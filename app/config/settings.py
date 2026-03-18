from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)

from app.config.app import AppConfig
from app.config.database import DatabaseConfig
from app.config.http import HttpConfig
from app.config.logging import LoggingConfig

CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"
YAML_DIR = CONFIG_DIR / "yaml"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FST_APP__",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_file=(
            ENVS_DIR / ".env.example",
            ENVS_DIR / ".env",
        ),
        yaml_config_section="fst",
        yaml_file=(
            YAML_DIR / "default.yaml",
            YAML_DIR / "local.yaml",
        )
    )
    app: AppConfig
    logging: LoggingConfig = LoggingConfig()
    database: DatabaseConfig
    http: HttpConfig = HttpConfig()

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            YamlConfigSettingsSource(
                settings_cls,
                deep_merge=True,
            ),
        )


settings = Settings()
