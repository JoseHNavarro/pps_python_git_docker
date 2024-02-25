# Fase de resolución de dependencias (basada en python:slim)
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Fase de ejecución (basada en la de resolución de dependencias)
FROM builder
COPY . .
CMD ["python", "app.py"]

