from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class AuditLog(BaseModel):
    __tablename__ = 'audit_logs'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    action = Column(String, nullable=False)
    ip_address = Column(String, nullable=True)
    details = Column(String, nullable=True)
    user = relationship("User", back_populates="audit_logs")
