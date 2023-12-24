from service.configs.setting import DB

from . import employee

search_employee_service = employee.search.init(DB)
