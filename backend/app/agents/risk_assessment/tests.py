import pytest
from app.agents.risk_assessment.agent import RiskAssessmentAgent
from app.agents.risk_assessment.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = RiskAssessmentAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
