from app.agents.qr_processing.schemas import InputSchema, OutputSchema
from app.agents.qr_processing.prompt import SYSTEM_PROMPT
from app.agents.qr_processing.tools import execute_tools

class QrProcessingAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
