FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: application image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY .env .env
COPY app/ app/

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]