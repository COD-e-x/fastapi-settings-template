from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from app.config.app import AppConfig
from app.config.database import DatabaseConfig
from app.config.http import HttpConfig
from app.config.logging import LoggingConfig

CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FST_APP__",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_file=(
            ENVS_DIR / ".env.example",
            ENVS_DIR / ".env",
        ),
    )
    app: AppConfig
    logging: LoggingConfig
    database: DatabaseConfig
    http: HttpConfig = HttpConfig()


settings = Settings()
