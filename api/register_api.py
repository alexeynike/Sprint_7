import allure

from api.base_api import BaseApi
from faker import Faker
from dataclasses import asdict
from models.user_modal import UserModel


class RegisterApi(BaseApi):
    @allure.step('Создание курьера')
    def create_courier(self, user_model: UserModel):
        return self.post(endpoint="/api/v1/courier", body=asdict(user_model))

    @allure.step('Проверка успешной регистрации нового пользователя')
    def assert_register_user_body(self):
        self.assert_body_is({"ok": True})

    @allure.step('Проверка отправки сообщения "Этот логин уже используется"')
    def assert_register_the_same_user_msg(self):
        self.assert_body_is({"message": "Этот логин уже используется"})

    @allure.step('Проверка отправки сообщения "Этот логин уже используется"')
    def assert_register_with_wrong_data_msg(self):
        self.assert_body_is({"message": "Недостаточно данных для создания учетной записи"})
