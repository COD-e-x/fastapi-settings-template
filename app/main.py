import logging

from fastapi import FastAPI
from app.config.settings import settings


logging.basicConfig(
    level=settings.logging.log_level,
)

app = FastAPI(
    title=settings.app.title,
)
