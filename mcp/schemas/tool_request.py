from pydantic import BaseModel
from typing import Dict, Any

class ToolRequest(BaseModel):
    tool: str
    args: Dict[str, Any]

class ToolResponse(BaseModel):
    tool: str
    status: str
    data: Dict[str, Any]
    error: str = None
