import logging
from flask import Flask, request, jsonify
import re
from tinydb import TinyDB

logging.basicConfig(level=logging.INFO)
logging.getLogger('werkzeug').setLevel(logging.DEBUG)

app = Flask(__name__)


def open_db():
    return TinyDB('forms_db.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    try:
        data = request.form.to_dict(flat=False)
        flattened_data = flatten_data(data)

        logging.info('Полученные данные: %s', flattened_data)

        template_name = find_matching_template(flattened_data)

        if template_name:
            logging.info('Соответствующий шаблон найден: %s', template_name)
            return jsonify({'template_name': template_name})
        else:
            field_types = infer_field_types(flattened_data)
            logging.info('Предполагаемые типы полей: %s', field_types)
            return jsonify(field_types)
    except Exception as e:
        logging.error('Ошибка обработки запроса: %s', e)
        return jsonify({'error': str(e)}), 500


def flatten_data(data):
    flattened_data = {}
    for key, value in data.items():
        if isinstance(value, list) and len(value) > 0:
            flattened_data[key] = value[0]
        else:
            flattened_data[key] = value
    return flattened_data


def find_matching_template(data):
    try:
        with open_db() as db:
            for template in db.all():
                template_fields = set(template.keys()) - {'name'}

                if template_fields.issubset(data.keys()):
                    if all(compare_field(data, field, template) for field in template_fields):
                        logging.info('Шаблон %s найден для данных %s', template['name'], data)
                        return template['name']
                else:
                    logging.info('Подходящий шаблон не найден для данных %s', data)

    except IOError as e:
        logging.error('Ошибка работы с базой данных: %s', e)
    return None


def compare_field(data, field, template):
    data_value = data.get(field, '')
    template_type = template.get(field, '')

    if not template_type:
        return False

    inferred_type = infer_field_type(data_value)

    return inferred_type == template_type


def infer_field_types(data):
    field_types = {}
    for field, value in data.items():
        field_type = infer_field_type(value)
        field_types[field] = field_type
    return field_types


def infer_field_type(value):
    if isinstance(value, dict):
        value = value.get('value', '')
    elif isinstance(value, list) and len(value) > 0:
        value = value[0]

    if is_valid_date(value):
        return 'date'
    elif is_valid_phone(value):
        return 'phone'
    elif is_valid_email(value):
        return 'email'
    else:
        return 'text'


def is_valid_date(date_string):
    date_regex = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.\d{4}$'
    return bool(re.match(date_regex, date_string))


def is_valid_phone(phone_number):
    phone_regex = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
    return bool(re.match(phone_regex, phone_number))


def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

