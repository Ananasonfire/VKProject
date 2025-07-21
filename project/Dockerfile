FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: final image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY .env ./
COPY alembic/ ./alembic/
COPY app/ ./app/
COPY Dockerfile .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]