from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    theme = Column(String, default='dark')
    language = Column(String, default='en')
    notifications = Column(Boolean, default=True)

    user = relationship('User', back_populates='settings')
