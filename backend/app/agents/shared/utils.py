import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_execution(message: str):
    logger.info(message)
