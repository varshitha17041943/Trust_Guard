import pytest
from app.agents.recommendation.agent import RecommendationAgent
from app.agents.recommendation.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = RecommendationAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
