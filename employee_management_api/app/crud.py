from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Employee, Department
from app.schemas import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, data: EmployeeCreate):

    department = db.get(
        Department,
        data.department_id
    )

    if not department:
        return None

    employee = Employee(
        name=data.name,
        email=data.email,
        salary=data.salary,
        department_id=data.department_id
    )

    try:
        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    except Exception:
        db.rollback()
        raise


def get_all_employees(db: Session):

    statement = select(Employee)

    return db.scalars(statement).all()


def get_employee(db: Session, employee_id: int):

    return db.get(Employee, employee_id)


def update_employee(
    db: Session,
    employee_id: int,
    data: EmployeeUpdate
):

    employee = db.get(Employee, employee_id)

    if not employee:
        return None

    updates = data.model_dump(exclude_unset=True)

    if "department_id" in updates:
        department = db.get(
            Department,
            updates["department_id"]
        )

        if not department:
            return None

    for key, value in updates.items():
        setattr(employee, key, value)

    try:
        db.commit()
        db.refresh(employee)

        return employee

    except Exception:
        db.rollback()
        raise


def delete_employee(db: Session, employee_id: int):

    employee = db.get(Employee, employee_id)

    if not employee:
        return False

    try:
        db.delete(employee)
        db.commit()

        return True

    except Exception:
        db.rollback()
        raise