import logging
from typing import Literal

from pydantic import BaseModel


class LoggingConfig(BaseModel):
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
    ] = "INFO"

    @property
    def log_level(self) -> int:
        return getattr(logging, self.level)

    def setup(self) -> None:
        logging.basicConfig(
            level=self.log_level,
            format=self.format,
        )
