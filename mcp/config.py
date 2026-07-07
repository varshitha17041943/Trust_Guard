from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MCP_API_KEY: str = "internal_mcp_key"
    VIRUSTOTAL_API_KEY: str = ""
    SAFE_BROWSING_API_KEY: str = ""
    CACHE_TTL_SECONDS: int = 86400

    class Config:
        env_file = ".env"

settings = Settings()
