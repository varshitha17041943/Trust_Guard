from app.agents.base import call_mcp_tool, AgentResponse
import asyncio

async def analyze_whois(target: str) -> AgentResponse:
    await asyncio.sleep(1) # simulate LLM thinking
    data = await call_mcp_tool("whois", target)
    risk = 0.8 if data.get("age_days", 100) < 30 else 0.1
    return AgentResponse(agent_name="WHOIS Analysis Agent", status="completed", finding=data, risk_score=risk)
