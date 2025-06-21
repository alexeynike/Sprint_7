import allure
import requests
from helpers.logger import *


class BaseApi:
    def __init__(self):
        self.base_url = " https://qa-scooter.praktikum-services.ru"
        self.response = None

    def _request(self, method=None, endpoint=None, data=None):
        logging_request(url=endpoint, method=method, data=data)
        self.response = requests.request(method=method, url=self.base_url + endpoint, json=data)
        logging_response(self.response)

    def get(self, endpoint: str):
        return self._request(method="GET", endpoint=endpoint)

    def post(self, endpoint, body):
        return self._request(method="POST", endpoint=endpoint, data=body)

    def delete(self, endpoint: str):
        return self._request(method="DELETE", endpoint=endpoint)

    def put(self, endpoint, body):
        return self._request(method="PUT", endpoint=endpoint, data=body)

    def get_data(self, keys):
        body = self.response.json()
        try:
            for key in keys:
                body = body[key]
            return body
        except KeyError:
            raise KeyError(f"По ключу {keys} значение отсутствует")

    @allure.step('Проверка статус кода')
    def assert_status_code_is(self, expected_code):
        assert expected_code == self.response.status_code, f"ОР: статус код {expected_code}\nФР: статус код {self.response.status_code}"

    @allure.step('Проверка тела ответа')
    def assert_body_is(self, data):
        assert self.response.json() == data, f"ОР: тело ответа равно: {data}\nФР: тело ответа: {self.response.json()}"

    @allure.step('Проверка наличия тела ответа')
    def assert_body_have(self, data):
        assert self.response.json().get(data) is not None, f"ОР: Тело ответа содержит поле {data}\nФР: Тело ответа{self.response.json()}"

    @allure.step('Проверка соответствия сообщения ОР')
    def assert_response_message(self, message: str):
        assert self.get_data(["message"]) == message
