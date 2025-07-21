FROM python:3.11-slim

WORKDIR /app

# Устанавливаем зависимости сразу
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем .env и код
COPY .env .env
COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
