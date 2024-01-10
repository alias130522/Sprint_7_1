import requests
from dataset import Url
import allure


class TestGettingListOrders:
    @allure.title('Получение списка заказов по id курьера')
    @allure.description("Проверка получения списка заказов по id курьера, в тело ответа возвращается список заказов")
    def test_getting_list_orders(self, courier_authorization):
        id_courier = courier_authorization.json()['id']
        response = requests.get(Url.url_getting_list_orders_courierId + str(id_courier))
        assert response.status_code == 200 and response.json()['orders'] == []

    @allure.title('Получение списка 10 доступных заказов для курьера')
    @allure.description("Проверка получения списка 10 доступных заказов для курьера")
    def test_getting_10_free_orders_from_list_orders(self):
        response = requests.get(Url.url_getting_10_free_orders)
        assert response.status_code == 200 and 'orders' in response.json()

    @allure.title('Получение списка заказов по указанию станции метро')
    def test_gettind_list_order_couriers_by_metro(self, courier_authorization):
        id_courier = courier_authorization.json()['id']
        response = requests.get(
            Url.url_getting_list_orders_courierId + str(id_courier) + Url.gettind_list_order_couriers_by_metro)
        assert response.json()['orders'] == [] and response.status_code == 200
