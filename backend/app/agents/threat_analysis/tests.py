import pytest
from app.agents.threat_analysis.agent import ThreatAnalysisAgent
from app.agents.threat_analysis.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = ThreatAnalysisAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
