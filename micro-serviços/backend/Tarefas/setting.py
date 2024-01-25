from typing import Any, Dict, Optional

from pydantic import AnyUrl, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MYSQL_SERVER: str
    FRONTEND_URL: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    TIMEZONE: str

    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return AnyUrl.build(
            scheme="mysql+pymysql",
            username=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("MYSQL_SERVER"),
            path=f"{values.get('MYSQL_DB')}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()