import requests
import allure
from dataset import Url
from helpers import random_pass, random_name, random_login


class TestCreatingCourier:
    @allure.title('Успешное создание курьера')
    @allure.description("Создание курьера, проверка кода и текста ответа")
    def test_can_create_courier(self):
        payload = {"login": random_login, "password": random_pass, "firstName": random_name}
        response = requests.post(Url.url_creating_courier, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Невозможно создать двух одинаковых курьеров")
    @allure.description("Проверка невозможности создания курьеров с одинаковыми логинами и паролями")
    def test_cannot_create_two_identical_couriers(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": register_new_courier_and_return_login_password[1],
                   "firstName": register_new_courier_and_return_login_password[2]}
        response = requests.post(Url.url_creating_courier, data=payload)
        assert response.status_code == 409 and response.text == ('{"code":409,"message":"Этот логин уже используется. '
                                                                 'Попробуйте другой."}')

    @allure.title("Попытка создать курьера без указания login")
    @allure.description("Проверка ответа при попытки создания курьера без обязательного поля login")
    def test_not_login_required_field(self):
        payload = {"password": random_pass, "firstName": random_name}
        response = requests.post(Url.url_creating_courier, data=payload)
        assert response.status_code == 400 and response.text == ('{"code":400,"message":"Недостаточно данных для '
                                                                 'создания учетной записи"}')

    @allure.title("Попытка создать курьера без указания password")
    @allure.description("Проверка ответа при попытки создания курьера без обязательного поля password")
    def test_not_password_required_field(self):
        payload = {"login": random_login, "firstName": random_name}
        response = requests.post(Url.url_creating_courier, data=payload)
        assert response.status_code == 400 and response.text == ('{"code":400,"message":"Недостаточно данных для '
                                                                 'создания учетной записи"}')
