from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/Alavancar'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'AshD7Xbyfk_cj3tInzI7gzhoaNg_F_yv_-iblxEkXjs'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class config:
        case_sensitive = True


settings: Settings = Settings()
