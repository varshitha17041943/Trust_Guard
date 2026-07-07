from app.agents.risk_assessment.schemas import InputSchema, OutputSchema
from app.agents.risk_assessment.prompt import SYSTEM_PROMPT
from app.agents.risk_assessment.tools import execute_tools

class RiskAssessmentAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
