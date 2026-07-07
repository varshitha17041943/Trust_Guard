import pytest
from app.agents.brand_analysis.agent import BrandAnalysisAgent
from app.agents.brand_analysis.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = BrandAnalysisAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
