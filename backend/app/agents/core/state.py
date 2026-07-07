from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class SharedContext(BaseModel):
    original_target: str
    scan_type: str
    normalized_url: Optional[str] = None
    
    # Security Findings
    ssl_valid: Optional[bool] = None
    whois_age_days: Optional[int] = None
    threat_intel_flags: List[str] = Field(default_factory=list)
    
    # Brand Verification
    impersonated_brand: Optional[str] = None
    official_url: Optional[str] = None
    
    # Risk Assessment
    risk_score: Optional[float] = None
    risk_level: Optional[str] = None
    confidence: Optional[float] = None
    
    # Output Generation (XAI)
    explanations: List[str] = Field(default_factory=list)
    learn_more_topics: List[Dict[str, str]] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    cyber_tip: Optional[str] = None
    raw_report: Optional[str] = None
