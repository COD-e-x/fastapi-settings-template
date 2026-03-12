from pydantic import BaseModel, SecretStr


class DatabaseConfig(BaseModel):
    database: str
    user: str
    password: SecretStr
    host: str
    port: int
    echo: bool = False
