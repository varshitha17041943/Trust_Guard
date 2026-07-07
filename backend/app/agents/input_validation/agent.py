from app.agents.input_validation.schemas import InputSchema, OutputSchema
from app.agents.input_validation.prompt import SYSTEM_PROMPT
from app.agents.input_validation.tools import execute_tools

class InputValidationAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
