# Stage 1: install dependencies
FROM python:3.11-slim AS builder
WORKDIR /app

# Сначала копируем только requirements, чтобы кешировать установку зависимостей
COPY requirements.txt ./
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: application image
FROM python:3.11-slim
WORKDIR /app

# Копируем уже установленный pip-пакеты из builder
COPY --from=builder /install /usr/local

# Копируем код приложения и .env
COPY .env .env
COPY app/ app/
COPY requirements.txt ./

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
