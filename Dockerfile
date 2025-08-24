FROM python:3.11-slim

# 1. Установим системные зависимости для mysqlclient
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       default-libmysqlclient-dev \
       pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# 2. Установим Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 3. Запуск gunicorn (Django через WSGI)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
