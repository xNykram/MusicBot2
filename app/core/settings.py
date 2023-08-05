import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RhenusBot"
    APP_ENV: str = os.environ.get("APP_ENV", "DEV")
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
    BOT_PREFIX: str = os.environ.get("BOT_PREFIX", "!")
    
