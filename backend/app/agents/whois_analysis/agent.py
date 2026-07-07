from app.agents.whois_analysis.schemas import InputSchema, OutputSchema
from app.agents.whois_analysis.prompt import SYSTEM_PROMPT
from app.agents.whois_analysis.tools import execute_tools

class WhoisAnalysisAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
