# LeadHit
# Web-приложение для определения заполненных форм

Это веб-приложение разработано на языке Python с использованием Flask для определения заполненных форм на основе заданных шаблонов. В качестве менеджера зависимостей используется Poetry.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/vmadiakin/LeadHit
    cd LeadHit
    ```

2. Установите зависимости:

    ```bash
    poetry install
    ```

3. Запустите веб-приложение:

    ```bash
    poetry run python app.py
    ```

## Использование

Веб-приложение ожидает POST запросы на урл `/get_form` с данными формы в теле запроса. Параметры формы передаются в виде `f_name1=value1&f_name2=value2`.

Пример использования с помощью `curl`:

```bash
curl -X POST -d "email=test@example.com&phone=+7%20987%20654%2032%2010" http://localhost:8080/get_form
```

# Тестовые запросы

В комплекте с проектом предоставлен скрипт `test_requests.py`, который содержит тестовые запросы для проверки функциональности приложения.

```bash
poetry run python test_requests.py
```

# Структура проекта

- `app.py`: Основной файл с кодом веб-приложения.
- `dbinsert.py`: Скрипт для вставки данных в базу данных.
- `forms_db.json`: Тестовая база данных с шаблонами форм.
- `test_requests.py`: Скрипт с тестовыми запросами для проверки приложения.

# Зависимости

Веб-приложение разработано на Python версии 3.11 и выше с использованием Poetry для управления зависимостями.

```toml
[tool.poetry.dependencies]
python = "^3.11"
flask = "^3.0.0"
tinydb = "^4.8.0"
requests = "^2.31.0"
```

