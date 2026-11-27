from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.models import Base
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app import crud

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Employee Management API is running"
    }


@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):

    employee = crud.create_employee(db, data)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return employee


@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db)
):

    return crud.get_all_employees(db)


@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = crud.get_employee(db, employee_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    employee = crud.update_employee(
        db,
        employee_id,
        data
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee or department not found"
        )

    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    result = crud.delete_employee(db, employee_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }