from app.agents.base import call_mcp_tool, AgentResponse
import asyncio

async def analyze_ssl(target: str) -> AgentResponse:
    await asyncio.sleep(1.2)
    data = await call_mcp_tool("ssl", target)
    risk = 0.0 if data.get("valid") else 1.0
    return AgentResponse(agent_name="SSL Analysis Agent", status="completed", finding=data, risk_score=risk)
