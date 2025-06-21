import allure
import pytest

@allure.title('Проверка создания заказа')
def test_make_valid_order(order_api, order_data):
    order_api.order(order_data)
    order_api.assert_status_code_is(201)
    order_api.assert_body_have("track")

@allure.title('Проверка создания заказа с использованием всех цветов самоката')
@pytest.mark.parametrize("colors", (["GREY"], ["BLACK"], ["GREY", "BLACK"], []))
def test_make_order_with_different_colors(order_api, order_data, colors):
    order_data.color = colors
    order_api.order(order_data)
    order_api.assert_status_code_is(201)

@allure.title('Проверка получения списка заказов')
def test_get_orders_list(order_api):
    order_api.get_orders_list()
    order_api.assert_status_code_is(200)
    order_api.assert_order_list_not_empty()
