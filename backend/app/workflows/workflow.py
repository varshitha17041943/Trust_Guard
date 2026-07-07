from app.workflows.executor import execute_antigravity_workflow

async def run_antigravity_workflow(scan_id: int, url: str, scan_type: str):
    return await execute_antigravity_workflow(scan_id, url, scan_type)
