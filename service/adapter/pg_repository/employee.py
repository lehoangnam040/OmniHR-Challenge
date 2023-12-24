from typing import Any

from service.usecases.employee.validators import SearchEmployeeRequest, SearchEmployeeResponse

from . import database


class PgEmployeeRepository:
    async def search_employees(
        self,
        request: SearchEmployeeRequest,
    ) -> list[SearchEmployeeResponse]:
        where_query_arr = ["e.id > :cursor_next"]
        query_args: dict[str, Any] = {
            "cursor_next": request.cursor_next,
            "limit": request.limit,
        }
        if request.statuses:
            where_query_arr.append("e.status = ANY(:statuses)")
            query_args["statuses"] = list(status.value for status in request.statuses)
        if request.companies:
            where_query_arr.append("d.company_id = ANY(:company_ids)")
            query_args["company_ids"] = request.companies
        if request.departments:
            where_query_arr.append("e.department_id = ANY(:department_ids)")
            query_args["department_ids"] = request.departments
        if request.locations:
            where_query_arr.append("e.location_id = ANY(:location_ids)")
            query_args["location_ids"] = request.locations
        if request.positions:
            where_query_arr.append("e.position_id = ANY(:position_ids)")
            query_args["position_ids"] = request.positions

        query = f"""
            SELECT
                e.id AS "id",
                e.first_name AS "first_name",
                e.last_name AS "last_name",
                e.email AS "email",
                e.phone_number AS "phone_number",
                e.status AS "status",
                d."name" AS "department_name",
                l."name" AS "location_name",
                p."name" AS "position_name"
            FROM employee e 
            LEFT JOIN department d ON e.department_id = d.id 
            LEFT JOIN "location" l ON e.location_id = l.id
            LEFT JOIN "position" p ON e.position_id = p.id
            WHERE
                {" AND ".join(where_query_arr)}
            ORDER BY id ASC
            LIMIT :limit
        """

        employees = []
        async for row in database.iterate(query=query, values=query_args):
            employees.append(SearchEmployeeResponse.parse_obj(row))
        return employees
