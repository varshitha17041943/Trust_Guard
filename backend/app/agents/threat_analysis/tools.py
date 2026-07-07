from app.agents.shared.utils import log_execution
import requests

def execute_tools(input_data):
    log_execution(f"Executing tools for {input_data.url} via MCP Server")

    import concurrent.futures
    
    def call_mcp(tool_name):
        try:
            resp = requests.post("http://localhost:8001/execute", headers={"x-api-key": "internal_mcp_key", "Content-Type": "application/json"}, json={"tool": tool_name, "args": {"url": input_data.url}})
            return resp.json().get("data", {})
        except:
            return {}

    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tools = ["virustotal", "safe_browsing", "openphish", "urlhaus"]
        futures = {executor.submit(call_mcp, t): t for t in tools}
        for future in concurrent.futures.as_completed(futures):
            t = futures[future]
            results[t] = future.result()
            
    return {"status": "success", "threat_data": results}

