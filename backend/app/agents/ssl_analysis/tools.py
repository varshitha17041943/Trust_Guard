from app.agents.shared.utils import log_execution
import requests

def execute_tools(input_data):
    log_execution(f"Executing tools for {input_data.url} via MCP Server")

    try:
        resp = requests.post("http://localhost:8001/execute", headers={"x-api-key": "internal_mcp_key", "Content-Type": "application/json"}, json={"tool": "ssl_checker", "args": {"url": input_data.url}})
        return resp.json().get("data", {"status": "error"})
    except Exception as e:
        log_execution(str(e))
        return {"status": "error"}

