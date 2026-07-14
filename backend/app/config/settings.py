import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "TrustGuardAI Enterprise API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite+aiosqlite:////tmp/trustguard.db" if os.environ.get("VERCEL") else "sqlite+aiosqlite:///./trustguard.db"
    ENVIRONMENT: str = "development"
    RATE_LIMIT_PER_MINUTE: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
