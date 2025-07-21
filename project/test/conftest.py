import os
import pytest

# Для тестов используем SQLite in-memory
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

from importlib import reload
# Перезагружаем конфигурацию и подключение к БД
import app.config; reload(app.config)
import app.db; reload(app.db)

from fastapi.testclient import TestClient
from app.main import app
from app.db import engine
from app.models import Base

@pytest.fixture(scope='session', autouse=True)
def init_db():
    # Сбрасываем и создаем схему
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    # Тестовый клиент FastAPI
    return TestClient(app)
