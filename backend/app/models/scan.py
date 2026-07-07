from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Scan(BaseModel):
    __tablename__ = 'scans'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    target = Column(String, nullable=False)
    scan_type = Column(String, nullable=False) # 'URL' or 'QR'
    status = Column(String, default='pending')
    risk_score = Column(Float, nullable=True)
    risk_level = Column(String, nullable=True)
    confidence_score = Column(Float, nullable=True)
    
    user = relationship("User", back_populates="scans")
    threat_results = relationship("ThreatResult", back_populates="scan", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="scan", cascade="all, delete-orphan")
    official_websites = relationship("OfficialWebsite", back_populates="scan", cascade="all, delete-orphan")
    threat_sources = relationship("ThreatSource", back_populates="scan", cascade="all, delete-orphan")
    embedding = relationship("Embedding", back_populates="scan", uselist=False, cascade="all, delete-orphan")
    report = relationship("Report", back_populates="scan", uselist=False, cascade="all, delete-orphan")
