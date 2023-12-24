from enum import Enum
from types import TracebackType

from pydantic import BaseModel


def trace_debugs(
    _: type[BaseException] | None,
    __: BaseException | None,
    tb: TracebackType | None,
) -> str:
    linenos = []
    while tb:
        linenos.append(tb.tb_lineno)
        tb = tb.tb_next
    return ".".join(map(str, linenos))


class ServiceError(BaseModel):
    error: Enum
    debug_id: str

