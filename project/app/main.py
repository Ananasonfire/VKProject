from fastapi import FastAPI
from .api import segments, users
from .db import engine
from .models import Base

app = FastAPI(
    title="VK User Segments Service",
    version="1.0",
    description="Сервис сегментирования пользователей"
)

# Health‑check endpoint
@app.get("/", tags=["health"])
async def health_check():
    return {"status": "ok"}

# Создаем таблицы при старте приложения
@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(bind=engine)

# Роутеры
app.include_router(segments.router)
app.include_router(users.router)
