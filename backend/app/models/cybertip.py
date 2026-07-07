from sqlalchemy import Column, String
from .base import BaseModel

class CyberTip(BaseModel):
    __tablename__ = 'cyber_tips'
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
