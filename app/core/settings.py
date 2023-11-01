import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RhenusBot"
    APP_ENV: str = os.environ.get("APP_ENV", "DEV")
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
    BOT_PREFIX: str = os.environ.get("BOT_PREFIX", "!")
    POSTGRES_URL: str = os.environ.get("POSTGRES_URL", None)

config = Settings()