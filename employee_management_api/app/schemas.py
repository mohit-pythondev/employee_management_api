from pydantic import BaseModel, EmailStr, Field, ConfigDict


class EmployeeCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    salary: int = Field(gt=0)

    department_id: int = Field(gt=0)


class EmployeeUpdate(BaseModel):

    name: str | None = Field(default=None, min_length=2, max_length=100)

    email: EmailStr | None = None

    salary: int | None = Field(default=None, gt=0)

    department_id: int | None = Field(default=None, gt=0)


class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    salary: int
    department_id: int

    model_config = ConfigDict(from_attributes=True)