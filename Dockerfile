# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем зависимости
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Копируем файлы приложения в образ
COPY app.py dbinsert.py forms_db.json /app/
COPY static /app/static

# Задаем рабочую директорию
WORKDIR /app

# Открываем порт 8080
EXPOSE 8080

# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]
