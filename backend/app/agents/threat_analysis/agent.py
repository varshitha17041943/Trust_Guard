from app.agents.threat_analysis.schemas import InputSchema, OutputSchema
from app.agents.threat_analysis.prompt import SYSTEM_PROMPT
from app.agents.threat_analysis.tools import execute_tools

class ThreatAnalysisAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
