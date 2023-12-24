from pydantic import BaseModel
from enum import Enum


class EmployeeStatus(Enum):

    ACTIVE = "ACTIVE"
    NOT_STARTED = "NOT_STARTED"
    TERMINATED = "TERMINATED"


class Employee(BaseModel):

    id: int
    first_name: str
    last_name: str
    email: str | None
    phone_number: str | None
    status: EmployeeStatus
    department_id: int | None
    location_id: int | None
    position_id: int | None
