from pydantic import BaseModel, SecretStr


class DatabaseConfig(BaseModel):
    db_database: str
    db_user: str
    db_password: SecretStr
    db_host: str
    db_port: int
    db_echo: bool = False
