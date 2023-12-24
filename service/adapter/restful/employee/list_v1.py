"""Login api v1 with username / password."""
from fastapi import APIRouter, Depends

from service.configs.exceptions import HttpServiceError
from service.configs.response import ErrorApiResponse, ListApiResponse
from service.usecases import search_employee_service
from service.usecases.employee.validators import (
    SearchEmployeeResponse,
    SearchEmployeeRequest,
)
from service.usecases.employee.errors import ErrorCode

router = APIRouter()


@router.get(
    "/v1/employees",
    responses={500: {"model": ErrorApiResponse}},
)
async def search_employee_v1(
    search_params: SearchEmployeeRequest = Depends(),
) -> ListApiResponse[SearchEmployeeResponse]:
    resp, err = await search_employee_service.logic(search_params)
    if err is None:
        return ListApiResponse(items=resp)

    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
