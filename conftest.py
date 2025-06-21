import pytest
from faker import Faker
from api.login_api import LoginApi
from api.order_api import OrderApi
from api.register_api import *
from models.order_model import OrderModel
from models.user_modal import UserModel
from datetime import date



@pytest.fixture
def register_api() -> RegisterApi:
    return RegisterApi()


@pytest.fixture
def login_api() -> LoginApi:
    return LoginApi()


@pytest.fixture
def order_api() -> OrderApi:
    return OrderApi()


@pytest.fixture
def user_model():
    faker = Faker()
    return UserModel(faker.user_name(), faker.password(length=6), faker.first_name())


@pytest.fixture
def login_user_model():
    return UserModel("usmith", "!m5R#y")


@pytest.fixture
def order_data():
    faker = Faker()
    faker.locale()
    return OrderModel(
        firstName=faker.first_name(),
        lastName=faker.last_name(),
        address=faker.address(),
        metroStation="Сокольники",
        phone=faker.numerify('+7 (###) ###-##-##'),
        rentTime=4,
        deliveryDate=date.today().isoformat(),
        comment=faker.text(max_nb_chars=30),
        color=["GRAY"]
    )
