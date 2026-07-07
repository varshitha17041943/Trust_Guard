import pytest
from app.agents.impl.agents import InputValidationAgent, RiskAssessmentAgent
from app.agents.core.state import SharedContext

@pytest.mark.asyncio
async def test_input_validation_agent(mock_context):
    agent = InputValidationAgent()
    mock_context.original_target = "https://EXAMPLE.com/path?tracker=123"
    
    result = await agent.execute(mock_context)
    assert result.normalized_url == "https://example.com/path"

@pytest.mark.asyncio
async def test_risk_assessment_critical(mock_context):
    agent = RiskAssessmentAgent()
    mock_context.threat_intel_flags = ["Flag 1"]
    mock_context.ssl_valid = False
    mock_context.whois_age_days = 5
    mock_context.impersonated_brand = "PayPal"
    
    result = await agent.execute(mock_context)
    assert result.risk_score == 70.0 # 35 + 15 + 10 + 10
    assert result.risk_level == "High"
