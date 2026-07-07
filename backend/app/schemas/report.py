from pydantic import BaseModel
from datetime import datetime

class ReportBase(BaseModel):
    scan_id: int
    pdf_path: str

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    generated_at: datetime

    class Config:
        from_attributes = True
