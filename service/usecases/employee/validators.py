from typing import Annotated

from pydantic import BaseModel
from fastapi import Query

from service.entity.employee import EmployeeStatus
from service.configs.setting import SETTINGS


class SearchEmployeeRequest(BaseModel):
    statuses: Annotated[list[EmployeeStatus] | None, Query()] = None
    locations: Annotated[list[int] | None, Query()] = None
    companies: Annotated[list[int] | None, Query()] = None
    departments: Annotated[list[int] | None, Query()] = None
    positions: Annotated[list[int] | None, Query()] = None
    cursor_next: int = 0
    limit: int = 50


class SearchEmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str | None
    phone_number: str | None
    status: EmployeeStatus
    department_name: str | None
    location_name: str | None
    position_name: str | None

    class Config:
        fields = {
            _field: {'exclude': True} for _field in SETTINGS.exclude_employee_fields
        }