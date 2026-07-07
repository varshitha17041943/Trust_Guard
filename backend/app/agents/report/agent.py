from app.agents.report.schemas import InputSchema, OutputSchema
from app.agents.report.prompt import SYSTEM_PROMPT
from app.agents.report.tools import execute_tools

class ReportAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
