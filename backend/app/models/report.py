from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Report(BaseModel):
    __tablename__ = 'reports'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    file_path = Column(String, nullable=False)
    status = Column(String, nullable=False)
    scan = relationship("Scan", back_populates="report")
