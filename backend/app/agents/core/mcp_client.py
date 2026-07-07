import httpx
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class MCPClient:
    def __init__(self, base_url: str = "http://localhost:8001", api_key: str = "mcp-super-secret-key"):
        self.base_url = base_url
        self.api_key = api_key
        
    async def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Any:
        async with httpx.AsyncClient() as client:
            try:
                logger.info(f"[MCP Client] Requesting {tool_name}")
                response = await client.post(
                    f"{self.base_url}/execute",
                    json={"tool_name": tool_name, "parameters": parameters},
                    headers={"X-MCP-API-Key": self.api_key},
                    timeout=15.0
                )
                response.raise_for_status()
                data = response.json()
                return data.get("data")
            except Exception as e:
                logger.error(f"[MCP Client] Tool {tool_name} failed: {e}")
                raise e

mcp_client = MCPClient()
