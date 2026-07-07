from fastapi import Request
from fastapi.responses import JSONResponse
from .custom import DomainException
from app.logging.logger import logger

async def domain_exception_handler(request: Request, exc: DomainException):
    logger.warning(f"Domain Error: {exc.code} - {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message, "code": exc.code}
    )

async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "code": "INTERNAL_ERROR"}
    )
