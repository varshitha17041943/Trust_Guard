import pytest
from app.agents.input_validation.agent import InputValidationAgent
from app.agents.input_validation.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = InputValidationAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
