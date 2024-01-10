import json
import pytest
import requests
import allure
from dataset import Url, DataOrder


class TestCreatingAnOrder:
    @allure.title('Успешное создание заказа')
    @allure.description("Создание заказа с изменением цвета самоката")
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    def test_true_creating_an_order(self, color):
        DataOrder.data_order["color"] = color
        payload = DataOrder.data_order
        response = requests.post(Url.url_creating_an_order, data=json.dumps(payload))
        assert response.status_code == 201 and "track" in response.text

