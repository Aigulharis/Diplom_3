import pytest
from selenium import webdriver
import allure
from urls import *
from data import Credentials
from pages.auth_page import AuthPage
from lokators.auth_page_locators import AuthLocators

@pytest.fixture(params=["chrome", "firefox"])
@allure.title('Фикстура для брайзеров')
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


@pytest.fixture
@allure.title('Фикстура создает заказ')
def create_order(driver):
    main_page = main_site(driver)
    main_page.wait_for_element(main_page.locators.BUTTON_CONSTRUCTOR) # Ждем загрузки страницы
    buns = main_page.driver.find_element(*main_page.locators.BUN_2)# Добавляем необходимые ингредиенты
    buns.click()
    sauces = main_page.driver.find_element(*main_page.locators.INGREDIENT_SAUCES_X)
    sauces.click()
    fillings = main_page.driver.find_element(*main_page.locators.INGREDIENT_FILLINGS_1)
    fillings.click()
    basket = main_page.driver.find_element(*main_page.locators.BASKET) # Переходим в корзину и оформляем заказ
    basket.click()
    order_button = main_page.driver.find_element(*main_page.locators.BUTTON_MAKE_ORDER)
    order_button.click()
    order_confirmation = main_page.wait_for_element(main_page.locators.ORDER_CONFIRMATION_WINDOW)# Ждём подтверждения заказа
    yield order_confirmation  # возвращаем объект окна подтверждения для тестов
    # После теста закрываем окно подтверждения
    close_button = main_page.driver.find_element(*main_page.locators.BUTTON_CLOSE_CONFIRMATION)
    close_button.click()

#def test_order_creation(create_order):
#    confirmation = create_order
#    assert "Заказ" in confirmation.text используем фикстуру для создания заказа
