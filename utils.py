import json
import re
import constants


def get_data_from_json(string: str) -> dict:
    return json.loads(string)


def get_json_from_data(data: dict) -> str:
    return json.dumps(data)


def get_phone_number(phone: str) -> str:
    phone_number = get_digits(phone)
    if len(phone_number) > constants.phone_number_length:
        phone_number = phone_number[constants.phone_number_length:]

    return phone_number


def get_digits(phone: str) -> str:
    result = ""
    match = re.finditer(r'(?:\d*)?', phone, flags=re.ASCII)
    for i in match:
        result += i[0]
    return result
