from tinydb import TinyDB, Query
import os

# Проверяем, существует ли файл с базой данных
db_filename = 'forms_db.json'
db_exists = os.path.isfile(db_filename)

# Создаем или подключаемся к базе данных
db = TinyDB(db_filename)

# Шаблон формы: Форма регистрации пользователя
user_registration_form = {
    "name": "User Registration Form",
    "user_name": "text",
    "email": "email",
    "phone_number": "phone",
    "birth_date": "date"
}

# Вставляем данные в базу данных
db.insert(user_registration_form)

# Шаблон формы: Форма заказа товара
order_form = {
    "name": "Order Form",
    "product_name": "text",
    "quantity": "text",
    "customer_name": "text",
    "customer_email": "email",
    "customer_phone": "phone"
}

# Вставляем данные в базу данных
db.insert(order_form)

# Шаблон формы: Форма обратной связи
feedback_form = {
    "name": "Feedback Form",
    "sender_name": "text",
    "sender_email": "email",
    "message": "text"
}

# Вставляем данные в базу данных
db.insert(feedback_form)

# Шаблон формы: Форма запланированного мероприятия
event_registration_form = {
    "name": "Event Registration Form",
    "event_name": "text",
    "event_date": "date",
    "participant_name": "text",
    "participant_email": "email",
    "participant_phone": "phone"
}

# Вставляем данные в базу данных
db.insert(event_registration_form)

# Закрываем соединение с базой данных, если она была создана в этом скрипте
if not db_exists:
    db.close()
