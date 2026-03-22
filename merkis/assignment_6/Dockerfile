FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir .

COPY main.py .
COPY ./data/best_model.pkl ./data/best_model.pkl

COPY ./data/encoder_ohe.pkl ./data/encoder_ohe.pkl

EXPOSE 8000

CMD ["uvicorn", "main:app" ,"--host", "127.0.0.1", "--port", "8000"]

