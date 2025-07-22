from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # единственная вещь, которой реально нужна в приложении
    database_url: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='',        # без префиксов
        extra='ignore',       # игнорировать все переменные, не описанные в модели
    )

    @field_validator('database_url')
    def validate_scheme(cls, v: str) -> str:
        # для sqlite-тестов — пропускаем
        if v.startswith('sqlite'):
            return v
        # для postgresql с psycopg2‑binary — обычный префикс
        assert v.startswith('postgresql://'), \
            "DATABASE_URL must start with postgresql://"
        return v

settings = Settings()

