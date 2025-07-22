from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    # остальное без изменений...

    class Config:
        env_file = '.env'
        model_config = {
            'populate_by_name': True,
            'env_prefix': ''
        }

    @field_validator('database_url')
    def validate_scheme(cls, v):
        # для тестов в памяти разрешаем sqlite://
        if v.startswith('sqlite'):
            return v
        # для всех остальных — должно начинаться с postgresql://
        assert v.startswith('postgresql://'), 'DATABASE_URL must start with postgresql://'
        return v

settings = Settings()
