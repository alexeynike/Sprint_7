import allure

from api.base_api import BaseApi
from models.order_model import OrderModel
from dataclasses import asdict


class OrderApi(BaseApi):
    @allure.step('Создание заказа')
    def order(self, order_model: OrderModel):
        self.post(endpoint="/api/v1/orders", body=asdict(order_model))

    @allure.step('Получение списка заказов')
    def get_orders_list(self):
        self.get(endpoint="/api/v1/orders")

    @allure.step('Проверка наличия списка заказов')
    def assert_order_list_not_empty(self):
        assert len(self.get_data(["orders"])) > 0, f'ОР: список заказов больше 0\n ФР: список заказов равен  {len(self.get_data(["orders"]))}'