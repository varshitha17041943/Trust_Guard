from app.agents.shared.utils import log_execution
import requests

def execute_tools(input_data):
    log_execution(f"Executing tools for {input_data.url} via MCP Server")

    try:
        resp1 = requests.post("http://localhost:8001/execute", headers={"x-api-key": "internal_mcp_key", "Content-Type": "application/json"}, json={"tool": "brand_similarity", "args": {"url": input_data.url}})
        resp2 = requests.post("http://localhost:8001/execute", headers={"x-api-key": "internal_mcp_key", "Content-Type": "application/json"}, json={"tool": "official_website", "args": {"url": input_data.url}})
        return {"similarity": resp1.json().get("data", {}), "official": resp2.json().get("data", {})}
    except Exception as e:
        log_execution(str(e))
        return {"status": "error"}

