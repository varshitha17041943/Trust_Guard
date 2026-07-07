from app.agents.recommendation.schemas import InputSchema, OutputSchema
from app.agents.recommendation.prompt import SYSTEM_PROMPT
from app.agents.recommendation.tools import execute_tools

class RecommendationAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
