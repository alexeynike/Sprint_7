import allure
import pytest

@allure.title('Проверка регистрации нового пользователя')
def test_create_new_user(register_api, user_model):
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(201)
    register_api.assert_register_user_body()

@allure.title('Проверка регистрации уже созданного пользователя')
@pytest.mark.xfail(reason="Дефект в теле ответа")
def test_create_the_same_user(register_api, user_model):
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(201)
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(409)
    register_api.assert_register_the_same_user_msg()

@allure.title('Проверка регистрации пользователя без поля login')
def test_create_user_without_login(register_api, user_model):
    user_model.login = ""
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(400)
    register_api.assert_response_message("Недостаточно данных для создания учетной записи")

@allure.title('Проверка регистрации пользователя без поля password')
def test_create_user_without_password(register_api, user_model):
    user_model.password = ""
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(400)
    register_api.assert_response_message("Недостаточно данных для создания учетной записи")

@allure.title('Проверка регистрации пользователя без поля firstName')
@pytest.mark.xfail(reason="Проходит регистрация без обязательного поля firstName")
def test_create_user_without_first_name(register_api, user_model):
    user_model.firstName = ""
    register_api.create_courier(user_model)
    register_api.assert_status_code_is(400)
    register_api.assert_response_message("Недостаточно данных для создания учетной записи")
