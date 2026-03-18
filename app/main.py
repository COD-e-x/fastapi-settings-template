import logging

from fastapi import FastAPI
from app.config.settings import settings

logger = logging.getLogger(__name__)
settings.logging.setup()

app = FastAPI(title=settings.app.title)

logger.info("Server started")

# DB connection test endpoint

from sqlalchemy import text
from app.database.engine import engine


@app.get("/test-db")
async def test_db():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        tables = await conn.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        ))
        return {
            "status": "ok",
            "tables": [row[0] for row in tables]
        }
