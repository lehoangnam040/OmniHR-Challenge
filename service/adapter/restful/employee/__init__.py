from fastapi import APIRouter

from . import list_v1

employee_router = APIRouter()
employee_router.include_router(list_v1.router)
