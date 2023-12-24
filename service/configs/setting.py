"""Global app settings."""
from typing import Any

from pydantic import BaseSettings, SecretStr
from enum import Enum


class SupportedDbType(Enum):
    POSTGRES = "postgres"


class Settings(BaseSettings):

    """Global app settings."""

    # Database
    db_host: str = "localhost"
    db_port: str = "15432"
    db_user: str = "postgres"
    db_pass: SecretStr = SecretStr("postgres")
    db_name: str = "postgres"
    exclude_employee_fields: set[str] = set()


    class Config:

        """Config of settings."""

        env_prefix = "SERVICE_"

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'exclude_employee_fields':
                return {x for x in raw_val.split(',')}
            return cls.json_loads(raw_val)


SETTINGS = Settings()
DB = SupportedDbType.POSTGRES
