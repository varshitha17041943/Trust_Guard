from pydantic import BaseModel
from typing import Optional

class SettingsBase(BaseModel):
    theme: str = 'dark'
    language: str = 'en'
    notifications: bool = True

class SettingsUpdate(BaseModel):
    theme: Optional[str] = None
    language: Optional[str] = None
    notifications: Optional[bool] = None

class SettingsResponse(SettingsBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
