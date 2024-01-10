import allure
import pytest
import requests
from dataset import Url, DataOrder


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description("Проверка кода ответа и возврата id курьера при успешной авторизации")
    def test_true_courier_authorization(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": register_new_courier_and_return_login_password[1]}
        response = requests.post(Url.url_courier_authorization, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Создание курьера без указания login')
    @allure.description("Проверка авторизации курьера без указания обязательного поля login")
    def test_courier_authorization_not_login(self, register_new_courier_and_return_login_password):
        payload = {"password": register_new_courier_and_return_login_password[1]}
        response = requests.post(Url.url_courier_authorization, data=payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Создание курьера без указания password')
    @allure.description("Проверка авторизации курьера без указания обязательного поля password")
    def test_courier_authorization_not_password(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0]}
        response = requests.post(Url.url_courier_authorization, data=payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Создание курьера с указанием неверных данных')
    @allure.description("Проверка авторизации курьера с неверным логином, паролем, парой догин-пароль")
    @pytest.mark.parametrize('wrong_data', [
        {"login": DataOrder.fix_list_data[0], "password": 'wrong_pass'},
        {"login": 'wrong_login', "password": DataOrder.fix_list_data[1]},
        {"login": 'wrong_login', "password": 'wrong_pass'}])
    def test_courier_authorization_wrong(self, wrong_data):
        payload = {"login": DataOrder.fix_list_data[0], "password": DataOrder.fix_list_data[1]}
        requests.post(Url.url_creating_courier, data=payload)
        payl = wrong_data
        response = requests.post(Url.url_courier_authorization, data=payl)
        assert response.text == '{"code":404,"message":"Учетная запись не найдена"}'
