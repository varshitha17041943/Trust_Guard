import asyncio
from abc import ABC, abstractmethod
from .state import SharedContext
import logging

logger = logging.getLogger(__name__)

class AgentBase(ABC):
    def __init__(self, name: str):
        self.name = name
        self.max_retries = 3

    @property
    @abstractmethod
    def prompt(self) -> str:
        pass

    @abstractmethod
    async def execute(self, context: SharedContext) -> SharedContext:
        pass
        
    async def run(self, context: SharedContext) -> SharedContext:
        for attempt in range(self.max_retries):
            try:
                logger.info(f"[{self.name}] Executing attempt {attempt + 1}")
                # Simulating LLM execution latency
                await asyncio.sleep(0.5)
                new_context = await self.execute(context)
                logger.info(f"[{self.name}] Completed successfully")
                return new_context
            except Exception as e:
                logger.error(f"[{self.name}] Error: {e}")
                if attempt == self.max_retries - 1:
                    raise e
                await asyncio.sleep(1)
        return context
