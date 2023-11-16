import requests
from urllib.parse import urlencode

url = 'http://127.0.0.1:5000/get_form'


def send_request(data, template_name):
    encoded_data = urlencode(data)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=encoded_data, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(f"Template Name: {result.get('template_name')}")
    return result.get('template_name')


def test_template(template_name, valid_data, invalid_data):
    print(f"\nTesting Template: {template_name}")

    # Тест с валидными данными
    result_valid = send_request(valid_data, template_name)
    assert result_valid == template_name, f"Test failed for {template_name} (Valid)"

    # Тест с невалидными данными
    if invalid_data is not None:
        result_invalid = send_request(invalid_data, template_name)
        assert result_invalid is None, f"Test failed for {template_name} (Invalid)"


# Тестовые запросы
data_user_registration_valid = {'user_name': 'John Doe', 'email': 'john.doe@example.com', 'phone_number': '+7 123 456 78 90', 'birth_date': '27.01.1992'}
data_user_registration_invalid = {'invalid_field': 'Invalid Data'}
test_template("User Registration Form", data_user_registration_valid, data_user_registration_invalid)

data_order_form_valid = {'product_name': 'Laptop', 'quantity': '2', 'customer_name': 'Bob', 'customer_email': 'bob@example.com', 'customer_phone': '+7 987 654 32 10'}
data_order_form_invalid = {'invalid_field': 'Invalid Data'}
test_template("Order Form", data_order_form_valid, data_order_form_invalid)

data_feedback_form_valid = {'sender_name': 'Alice', 'sender_email': 'alice@example.com', 'message': 'Great service!'}
data_feedback_form_invalid = {'invalid_field': 'Invalid Data'}
test_template("Feedback Form", data_feedback_form_valid, data_feedback_form_invalid)

data_event_registration_form_valid = {'event_name': 'Conference', 'event_date': '27.01.2023', 'participant_name': 'Eve', 'participant_email': 'eve@example.com', 'participant_phone': '+7 876 543 21 09'}
data_event_registration_form_invalid = {'invalid_field': 'Invalid Data'}
test_template("Event Registration Form", data_event_registration_form_valid, data_event_registration_form_invalid)

print("All tests passed successfully.")
