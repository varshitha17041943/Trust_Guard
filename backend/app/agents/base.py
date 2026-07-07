import os
from pydantic import BaseModel
import httpx

class AgentResponse(BaseModel):
    agent_name: str
    status: str
    finding: dict
    risk_score: float

async def call_mcp_tool(tool_name: str, target: str):
    mcp_url = os.getenv("MCP_URL", "http://localhost:8001/execute")
    api_key = os.getenv("MCP_API_KEY", "mcp_secret")
    async with httpx.AsyncClient() as client:
        resp = await client.post(mcp_url, json={"tool": tool_name, "target": target}, headers={"X-MCP-API-KEY": api_key})
        return resp.json().get("data", {})
