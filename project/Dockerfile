# Stage 1: install dependencies
FROM python:3.11-slim AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt ./

# Устанавливаем зависимости в отдельный префикс, чтобы кэшировать
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: application image
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости из builder
COPY --from=builder /install /usr/local

# Копируем конфигурационный файл и код приложения
COPY .env .env
COPY app/ app/

# Запускаем приложение через Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]