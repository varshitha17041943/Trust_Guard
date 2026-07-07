import pytest
from app.agents.whois_analysis.agent import WhoisAnalysisAgent
from app.agents.whois_analysis.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = WhoisAnalysisAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
