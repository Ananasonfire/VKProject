from pydantic import  field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    class Config:
        env_file = '.env'
        model_config = {
            'populate_by_name': True,
            'env_prefix': ''
        }

    @field_validator('database_url')
    def ensure_psycopg2(cls, v):
        assert 'postgresql+' in v, 'DATABASE_URL must use psycopg driver'
        return v

settings = Settings()