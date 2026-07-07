import asyncio
from app.workflows.workflow_config import TIMEOUT_SECONDS

async def with_timeout(func, *args, **kwargs):
    try:
        return await asyncio.wait_for(func(*args, **kwargs), timeout=TIMEOUT_SECONDS)
    except asyncio.TimeoutError:
        raise Exception(f"Function {func.__name__} timed out after {TIMEOUT_SECONDS}s")
