from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from datetime import datetime

class WorkflowState(BaseModel):
    scan_id: int
    url: str
    scan_type: str = "website"
    current_stage: str = "Initializing"
    completed_stages: List[str] = []
    progress_percentage: int = 0
    estimated_time_remaining: str = "00:10"
    agent_outputs: Dict[str, Any] = {}
    errors: List[str] = []
    retry_count: int = 0
    final_result: Optional[Dict[str, Any]] = None
    start_time: datetime = datetime.utcnow()
