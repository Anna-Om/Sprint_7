import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_with_static_data():
    payload = {
        "login": 'Saymyo',
        "password": '123456',
        "firstName": 'Samuel'
    }
    return payload