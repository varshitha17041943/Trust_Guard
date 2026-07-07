import asyncio
import logging
from app.workflows.workflow_config import MAX_RETRIES

logger = logging.getLogger(__name__)

async def with_retry(func, *args, **kwargs):
    retries = 0
    while retries <= MAX_RETRIES:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            retries += 1
            logger.warning(f"Error in {func.__name__}: {e}. Retry {retries}/{MAX_RETRIES}")
            if retries > MAX_RETRIES:
                logger.error(f"Failed after {MAX_RETRIES} retries.")
                raise e
            await asyncio.sleep(1)
