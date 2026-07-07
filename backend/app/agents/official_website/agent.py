from app.agents.official_website.schemas import InputSchema, OutputSchema
from app.agents.official_website.prompt import SYSTEM_PROMPT
from app.agents.official_website.tools import execute_tools

class OfficialWebsiteAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
