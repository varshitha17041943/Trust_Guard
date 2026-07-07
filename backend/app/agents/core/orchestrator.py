from .state import SharedContext
import asyncio
import logging

logger = logging.getLogger(__name__)

class DAGOrchestrator:
    def __init__(self, agents_map: dict):
        # agents_map: {"phase1": [Agent1], "phase2": [Agent2, Agent3], ...}
        self.agents_map = agents_map

    async def run(self, initial_context: SharedContext) -> SharedContext:
        context = initial_context
        
        for phase, agents in self.agents_map.items():
            logger.info(f"--- Starting {phase} ---")
            # Run agents in the current phase concurrently
            tasks = [agent.run(context.model_copy(deep=True)) for agent in agents]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Merge state
            for result in results:
                if isinstance(result, Exception):
                    logger.error(f"Agent failed: {result}")
                else:
                    # For a real implementation, write a deep merge. Here we do simple overwrite for non-nulls.
                    for key, val in result.model_dump().items():
                        if val is not None and (not isinstance(val, list) or len(val) > 0):
                            setattr(context, key, val)
                            
        logger.info("--- Orchestration Complete ---")
        return context
