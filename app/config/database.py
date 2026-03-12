from pydantic import BaseModel, SecretStr
from sqlalchemy import URL


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False


class DatabaseConfig(BaseModel):
    username: str
    password: SecretStr
    host: str
    port: int
    database: str

    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    @property
    def asyncpg_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.database,

        )
