import pytest
from app.agents.explanation.agent import ExplanationAgent
from app.agents.explanation.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = ExplanationAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
