from app.agents.brand_analysis.schemas import InputSchema, OutputSchema
from app.agents.brand_analysis.prompt import SYSTEM_PROMPT
from app.agents.brand_analysis.tools import execute_tools

class BrandAnalysisAgent:
    async def execute(self, input_data: InputSchema) -> OutputSchema:
        # Mocking LLM Execution with tools
        result = execute_tools(input_data)
        return OutputSchema(**result)
