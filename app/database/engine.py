from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config.settings import settings

engine = create_async_engine(
    url=settings.database.asyncpg_url,
    echo=settings.database.sqla.echo,
    connect_args = {"server_settings": {"timezone": "UTC"}},
)
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
