from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class Embedding(BaseModel):
    __tablename__ = 'embeddings'
    scan_id = Column(Integer, ForeignKey('scans.id'), nullable=False)
    vector = Column(JSON, nullable=False) # Fallback to JSON for SQLite compatibility
    scan = relationship("Scan", back_populates="embedding")
