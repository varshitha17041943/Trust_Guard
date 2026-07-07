from app.agents.orchestrator.workflow import Orchestrator
from app.agents.shared.schemas import ScanRequest, FinalReport

async def run_scan_workflow(url: str, scan_type: str = "website") -> FinalReport:
    orchestrator = Orchestrator()
    return await orchestrator.execute_scan(ScanRequest(url=url, scan_type=scan_type))
