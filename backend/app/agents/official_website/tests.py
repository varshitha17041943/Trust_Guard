import pytest
from app.agents.official_website.agent import OfficialWebsiteAgent
from app.agents.official_website.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = OfficialWebsiteAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
