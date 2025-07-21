from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from .config import settings



DATABASE_URL = settings.database_url

if DATABASE_URL.startswith("sqlite"):
    # In‑memory SQLite для тестов
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=False,
        future=True,
    )
else:
    # PostgreSQL (или другая внешняя БД)
    engine = create_engine(
        DATABASE_URL,
        future=True,
        echo=False,
    )

# Фабрика сессий
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)
