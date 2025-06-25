import pytest
from selenium import webdriver
import allure
from pages.auth_page import AuthPage
from data import *
import requests


@pytest.fixture(params=["chrome", "firefox"])
@allure.title('Фикстура для браузеров')
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)

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
