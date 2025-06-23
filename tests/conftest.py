import pytest
from selenium import webdriver
import allure
from pages.auth_page import AuthPage
from lokators.auth_page_locators import AuthLocators
from seletools.actions import drag_and_drop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lokators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import *
from urls import Url, ApiUrl
import requests


@pytest.fixture(params=["chrome", "firefox"])
@allure.title('Фикстура для брайзеров')
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)
        #driver.get(MANE_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)
        #driver.get(MANE_SITE)

    yield driver
    driver.quit()

@pytest.fixture()
@allure.title('Фикстура на авторизацию')
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    auth_page = AuthPage(driver)
    auth_page.auth(Credentials.EMAIL,Credentials.PASSWORD)
    yield driver
    # после теста выход
    #auth_page.click_on_element(AuthLocators.EXIT_BUTTON)

@pytest.fixture(scope="function")
def create_user():
    auth_data_register = {
        "email": DataUser.DATA_USER["email"],
        "password": DataUser.DATA_USER["password"],
        "name": DataUser.DATA_USER["name"]
    }
    with allure.step('Создаём пользователя через fixture'):
        response = requests.post(Url.REGISTER_URL, json=auth_data_register)
        # Проверяем статус, чтобы fixture отработала как ожидается
        assert response.status_code == 200
        response_body = response.json()

        yield auth_data_register, response_body

        access_token = response_body['accessToken']
        requests.delete(Url.USER_DELETE_URL, headers={'Authorization': access_token})