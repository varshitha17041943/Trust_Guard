import pytest
from app.agents.qr_processing.agent import QrProcessingAgent
from app.agents.qr_processing.schemas import InputSchema

@pytest.mark.asyncio
async def test_agent():
    agent = QrProcessingAgent()
    result = await agent.execute(InputSchema(url="https://example.com"))
    assert result.status == "success"
