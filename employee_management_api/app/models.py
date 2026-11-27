from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


class Base(DeclarativeBase):
    pass


class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    employees: Mapped[list["Employee"]] = relationship(
        back_populates="department"
    )


class Employee(Base):

    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    salary: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )

    department: Mapped["Department"] = relationship(
        back_populates="employees"
    )