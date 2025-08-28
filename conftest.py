import pytest
import requests
from urls import Urls
from helpers import generate_random_string


@pytest.fixture
def courier():
    courier_data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(6)
    }
    response = requests.post(Urls.URL_CREATE_COURIER, json=courier_data)

    yield courier_data, response

    # Удаление курьера после теста
    login_response = requests.post(Urls.URL_LOGIN_COURIER, json={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        requests.delete(f"{Urls.URL_CREATE_COURIER}/{courier_id}")