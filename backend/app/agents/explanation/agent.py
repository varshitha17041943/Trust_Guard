from app.agents.explanation.schemas import InputSchema, OutputSchema
from app.agents.explanation.prompt import SYSTEM_PROMPT
from app.agents.explanation.tools import execute_tools

class ExplanationAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
