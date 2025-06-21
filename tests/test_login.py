from api.login_api import *

@allure.title('Проверка авторизации курьера')
def test_login_valid_user(login_api, login_user_model):
    login_api.login(login_user_model)
    login_api.assert_status_code_is(200)
    login_api.assert_user_is_loged_in()

@allure.title('Проверка авторизации курьера с невалидным login')
def test_login_with_wrong_login(login_api, login_user_model):
    login_user_model.login = login_user_model.login[1:]
    login_api.login(login_user_model)
    login_api.assert_status_code_is(404)
    login_api.assert_response_message("Учетная запись не найдена")

@allure.title('Проверка авторизации курьера с невалидным password')
def test_login_with_wrong_password(login_api, login_user_model):
    login_user_model.login = login_user_model.password[1:]
    login_api.login(login_user_model)
    login_api.assert_status_code_is(404)
    login_api.assert_response_message("Учетная запись не найдена")

@allure.title('Проверка авторизации курьера без поля login')
def test_login_without_login(login_api, login_user_model):
    login_user_model.login = None
    login_api.login(login_user_model)
    login_api.assert_status_code_is(400)
    login_api.assert_response_message("Недостаточно данных для входа")

@allure.title('Проверка авторизации курьера без поля password')
def test_login_without_password(login_api, login_user_model):
    login_user_model.password = None
    login_api.login(login_user_model)
    login_api.assert_status_code_is(400)
    login_api.assert_response_message("Недостаточно данных для входа")

