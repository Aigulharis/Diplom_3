import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#from curl import *
from data import Credentials
from pages.auth_page import AuthPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)
        #driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.set_window_size(1920, 1080)
        #driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    auth_page = AuthPage(driver)
    auth_page.auth(Credentials.EMAIL,Credentials.PASSWORD)

    return driver
