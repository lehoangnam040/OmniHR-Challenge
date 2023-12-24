from typing import Protocol, runtime_checkable

from .validators import SearchEmployeeRequest, SearchEmployeeResponse


@runtime_checkable
class SearchEmployeeRepository(Protocol):
    async def search_employees(
        self,
        request: SearchEmployeeRequest,
    ) -> list[SearchEmployeeResponse]:
        ...
