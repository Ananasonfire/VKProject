from fastapi import FastAPI
from .api import segments, users
from .db import engine
from .models import Base
from .core.logger import configure_logging

# создаем таблицы при старте (либо используем alembic)
Base.metadata.create_all(bind=engine)

configure_logging()
app = FastAPI(
    title='VK User Segments Service',
    version='1.0.0',
)
app.include_router(segments.router)
app.include_router(users.router)