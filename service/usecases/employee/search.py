from service.configs.setting import SupportedDbType
from service.configs.typing_compat import ResultWithErr
from service.usecases.employee.repository import SearchEmployeeRepository
from service.usecases.employee.validators import (
    SearchEmployeeRequest,
    SearchEmployeeResponse,
)

def _repository_factory(db_type: SupportedDbType) -> SearchEmployeeRepository:
    if db_type == SupportedDbType.POSTGRES:
        from service.adapter.pg_repository.employee import PgEmployeeRepository

        return PgEmployeeRepository()
    raise NotImplementedError


def init(
    db_type: SupportedDbType,
) -> "SearchEmployee":
    return SearchEmployee(_repository_factory(db_type))


class SearchEmployee:
    def __init__(
        self,
        repository: SearchEmployeeRepository,
    ) -> None:
        self.repository = repository

    async def logic(
        self,
        request: SearchEmployeeRequest,
    ) -> ResultWithErr[list[SearchEmployeeResponse]]:
        employees = await self.repository.search_employees(request)
        return employees, None
        
