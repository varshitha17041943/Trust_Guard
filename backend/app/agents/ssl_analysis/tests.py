import pytest
from app.agents.ssl_analysis.agent import SslAnalysisAgent
from app.agents.ssl_analysis.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = SslAnalysisAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
