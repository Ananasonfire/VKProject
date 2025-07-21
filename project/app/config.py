from pydantic import BaseSettings, field_validator

class Settings(BaseSettings):
    database_url: str

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