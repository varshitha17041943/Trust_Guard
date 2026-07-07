from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import Any, Dict
import httpx
import asyncio
from tools.registry import tool_registry

app = FastAPI(title="TrustGuardAI MCP Server", version="1.0.0")

API_KEY_NAME = "X-MCP-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)
VALID_API_KEY = "mcp-super-secret-key"

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate MCP API KEY")
    return api_key

class ToolRequest(BaseModel):
    tool_name: str
    parameters: Dict[str, Any]

@app.post("/execute")
async def execute_tool(request: ToolRequest, api_key: str = Depends(verify_api_key)):
    if request.tool_name not in tool_registry:
        raise HTTPException(status_code=404, detail=f"Tool {request.tool_name} not found")
        
    tool = tool_registry[request.tool_name]
    try:
        # Validate input schema
        validated_input = tool.input_schema(**request.parameters)
        # Execute with retry policy & caching
        result = await tool.execute_with_retry(validated_input)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tools")
async def list_tools(api_key: str = Depends(verify_api_key)):
    return {"tools": list(tool_registry.keys())}
