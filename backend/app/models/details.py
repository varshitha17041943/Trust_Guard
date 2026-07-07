from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class ThreatResult(BaseModel):
    __tablename__ = 'threat_results'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    agent_name = Column(String, nullable=False)
    status = Column(String, nullable=False) # Fail/Warn/Pass
    description = Column(String, nullable=False)
    passed = Column(Boolean, nullable=False)
    scan = relationship("Scan", back_populates="threat_results")

class Recommendation(BaseModel):
    __tablename__ = 'recommendations'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    text = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    scan = relationship("Scan", back_populates="recommendations")

class OfficialWebsite(BaseModel):
    __tablename__ = 'official_websites'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    brand_name = Column(String, nullable=False)
    official_url = Column(String, nullable=False)
    scan = relationship("Scan", back_populates="official_websites")

class ThreatSource(BaseModel):
    __tablename__ = 'threat_sources'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    source_name = Column(String, nullable=False)
    reference_url = Column(String, nullable=True)
    scan = relationship("Scan", back_populates="threat_sources")
