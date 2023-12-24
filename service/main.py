"""Entrypoint of service."""
import logging
import time
import asyncio

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from service.configs.response import ErrorApiResponse
from service import __version__
from service.configs.exceptions import setup_exception_handlers
from service.configs.setting import SETTINGS
from service.adapter.restful import api_router
from service.adapter.pg_repository import (
    connect_pg_database,
    disconnect_pg_database,
    setup_pg_database_connection,
)
from service.adapter.vendor.rate_limiter import RateLimiter

logging.getLogger().setLevel(logging.INFO)
logging.info("App settings %s", SETTINGS)
app = FastAPI(version=__version__)
rate_limiter = RateLimiter()

setup_exception_handlers(app)
setup_pg_database_connection(app)

app.include_router(api_router)

@app.middleware("http")
async def rate_limit_api(request: Request, call_next):
    request_identifier = request.client.host
    if not rate_limiter.is_this_request_valid(request_identifier):
        return JSONResponse(
            status_code=403,
            content=jsonable_encoder(
                ErrorApiResponse(
                    code="E0002",
                    message="Rate limit",
                    debug_id="",
                ),
            ),
        )
    unix_ts_of_request = time.time()
    rate_limiter.inc(request_identifier, unix_ts_of_request)
    response = await call_next(request)
    rate_limiter.dec(request_identifier, unix_ts_of_request)
    return response

@app.on_event("startup")
async def startup() -> None:
    """Run when starting service."""
    await connect_pg_database(app.state.database)


@app.on_event("shutdown")
async def shutdown() -> None:
    """Run when closing service."""
    await disconnect_pg_database(app.state.database)


@app.get("/")
async def main() -> str:
    """Home page of service."""
    return "Service"


@app.get("/health")
async def health() -> dict:
    """Return health status of service."""
    await asyncio.sleep(1)
    return {"status": "OK"}
