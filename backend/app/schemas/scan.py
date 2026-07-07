from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLScanRequest(BaseModel):
    target_url: HttpUrl

class QRScanRequest(BaseModel):
    qr_data: str

class ScanResponse(BaseModel):
    id: int
    target: str
    scan_type: str
    status: str
    risk_score: Optional[float]
    created_at: datetime
    class Config:
        from_attributes = True
