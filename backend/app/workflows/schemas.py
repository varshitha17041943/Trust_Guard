from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class FinalResponseSchema(BaseModel):
    scan_id: int
    url: str
    risk_score: int
    risk_level: str
    confidence_score: int
    quick_decisions: Dict[str, str]
    findings: List[Dict[str, str]]
    learn_more: List[Dict[str, str]]
    recommendations: List[str]
    official_website: Dict[str, Any]
    report: Dict[str, str]
    execution: Dict[str, Any]
