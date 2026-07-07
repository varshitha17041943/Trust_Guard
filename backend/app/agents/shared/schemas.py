from pydantic import BaseModel
from typing import Optional, List, Dict

class ScanRequest(BaseModel):
    url: str
    scan_type: str = "website"

class FinalReport(BaseModel):
    url: str
    risk_score: int
    risk_level: str
    confidence: int
    quick_decisions: Dict[str, str]
    findings: List[Dict[str, str]]
    recommendations: List[str]
    official_website: str
    report_id: str
    generated_at: str
