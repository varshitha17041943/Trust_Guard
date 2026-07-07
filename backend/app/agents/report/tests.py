import pytest
from app.agents.report.agent import ReportAgent
from app.agents.report.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = ReportAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
