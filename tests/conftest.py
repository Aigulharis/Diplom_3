import pytest
from selenium import webdriver
import allure
from data import Credentials
from pages.auth_page import AuthPage
from lokators.auth_page_locators import AuthLocators
from seletools.actions import drag_and_drop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lokators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


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
    """
    Фикстура для создания заказа на главной странице.
    Предполагается, что пользователь уже авторизован.
    Добавляет ингредиент в корзину и оформляет заказ.
    """
    main_page = MainPage(driver)
    main_page.click_on_button_constructor()
    main_page.main_page_loading_wait()  # ждём загрузку и скрытие оверлея

    # Перетащить ингредиент
    main_page.drag_and_drop_ingredient_to_order()

    # Нажать кнопку "Оформить заказ"
    button_order = driver.find_element(*main_page.locators.BUTTON_MAKE_ORDER)
    button_order.click()

    # Ждём появления окна с подтверждением заказа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_ID_CONFIRMATION_WINDOW)
    )

    yield driver

    # По окончании теста закрываем окно подтверждения (кнопка крестик)
    close_button = driver.find_element(*MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
    close_button.click()
