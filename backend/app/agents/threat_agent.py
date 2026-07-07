from app.agents.base import call_mcp_tool, AgentResponse
import asyncio

async def analyze_threat(target: str) -> AgentResponse:
    await asyncio.sleep(1.5)
    data = await call_mcp_tool("threat", target)
    risk = 0.9 if data.get("listed_in_phishing_db") else 0.0
    return AgentResponse(agent_name="Threat Intel Agent", status="completed", finding=data, risk_score=risk)
