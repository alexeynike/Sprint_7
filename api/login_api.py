import allure

from api.base_api import BaseApi
from models.user_modal import UserModel
from dataclasses import asdict


class LoginApi(BaseApi):
    @allure.step('Авторизация пользователя')
    def login(self, user_model: UserModel):
        self.post("/api/v1/courier/login", body=asdict(user_model))

    @allure.step('Проверка успешной авторизации пользователя')
    def assert_user_is_loged_in(self):
        self.assert_body_is({"id": 548405})
