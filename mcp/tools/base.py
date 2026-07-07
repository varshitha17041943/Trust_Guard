from abc import ABC, abstractmethod
from pydantic import BaseModel
import logging
import asyncio
import time

logger = logging.getLogger("mcp_tool")

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = 0
        self.state = "CLOSED"

    def record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            logger.warning("Circuit Breaker TRIPPED to OPEN state.")

    def record_success(self):
        self.failures = 0
        self.state = "CLOSED"

    def is_allowed(self) -> bool:
        if self.state == "CLOSED":
            return True
        if self.state == "OPEN" and time.time() - self.last_failure_time > self.recovery_timeout:
            self.state = "HALF-OPEN"
            return True
        return False

class BaseTool(ABC):
    name: str
    input_schema: type[BaseModel]
    output_schema: type[BaseModel]
    
    def __init__(self):
        self.max_retries = 3
        self._cache = {}
        self.circuit_breaker = CircuitBreaker()
        
    @abstractmethod
    async def execute(self, params: BaseModel) -> BaseModel:
        pass
        
    @abstractmethod
    def fallback(self, params: BaseModel) -> BaseModel:
        pass
        
    async def execute_with_retry(self, params: BaseModel) -> dict:
        cache_key = params.model_dump_json()
        if cache_key in self._cache:
            return self._cache[cache_key]
            
        if not self.circuit_breaker.is_allowed():
            logger.warning(f"[{self.name}] Circuit OPEN. Using fallback.")
            return self.fallback(params).model_dump()
            
        for attempt in range(self.max_retries):
            try:
                result = await asyncio.wait_for(self.execute(params), timeout=10.0)
                self.circuit_breaker.record_success()
                out_dict = result.model_dump()
                self._cache[cache_key] = out_dict
                return out_dict
            except Exception as e:
                logger.error(f"[{self.name}] Error: {e}")
                if attempt == self.max_retries - 1:
                    self.circuit_breaker.record_failure()
                    return self.fallback(params).model_dump()
                await asyncio.sleep(2 ** attempt)
