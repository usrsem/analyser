import os
import pydantic as pc
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # pg_host: str = Field(..., env="PG_HOST")
    pg_host: str = os.getenv(BaseSettings.Config.env_prefix + "PG_HOST")
    pg_user: str = os.getenv(BaseSettings.Config.env_prefix + "PG_USER")
    pg_password: str = os.getenv(BaseSettings.Config.env_prefix + "PG_PASSWORD")
    pg_db_name: str = os.getenv(BaseSettings.Config.env_prefix + "PG_DB_NAME")

    class Config:
        env_prefix = 'ANALYSER_'


settings = Settings()


DEFAULT_PG_URL = "postgresql://postgres:password@localhost/enrollment"
ASYNC_DEFAULT_PG_URL = "postgresql+asyncpg://postgres:password@localhost/enrollment"

