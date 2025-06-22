from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
from data import Credentials
from pages.main_page import MainPage
from lokators.main_page_locators import MainPageLocators
from lokators.auth_page_locators import AuthLocators
from urls import main_site
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains

class TestCheckingBasicFunctions:

    @allure.title('Проверяем переход в раздел "Лента заказов" без авторизации с главной страницы')
    def test_order_feed_access_without_auth(self, driver):  # фикстура только с driver без авторизации
        wait = WebDriverWait(driver, 10)

        with allure.step('Переход в раздел "Лента заказов"'):
            order_feed_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_FEED))
            order_feed_btn.click()

        with allure.step('Проверка открытия раздела "Лента заказов"'):
            order_feed_header = wait.until(EC.visibility_of_element_located(MainPageLocators.BUTTON_ORDER_FEED))
            assert order_feed_header.is_displayed(), "Не открылся раздел 'Лента заказов' после перехода"

    @allure.title('Проверяем переход по клику в раздел "Лента заказов после авторизации в личном кабинете')
    def test_login_in_order_fee_through_personal_account_auth(self, login):  # Используем login вместо driver
        driver = login  # фикстура возвращает driver после авторизации
        wait = WebDriverWait(driver, 10)

        with allure.step('Переход в раздел "Лента заказов"'):
            order_feed_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_FEED))
            order_feed_btn.click()

        with allure.step('Проверка открытия раздела "Лента заказов"'):
            order_feed_header = wait.until(EC.visibility_of_element_located(MainPageLocators.BUTTON_ORDER_FEED))
            assert order_feed_header.is_displayed(), "Не открылся раздел 'Лента заказов' после перехода"


    @allure.title('Переход в раздел "Конструктор" с раздела "Лента Заказов"')
    def test_going_to_the_constructor_section(self, driver):
        wait = WebDriverWait(driver, 10)

        with allure.step('Переход в раздел "Лента заказов"'):
            order_feed_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_FEED))
            order_feed_btn.click()

        with allure.step('Проверка открытия раздела "Лента заказов"'):
            order_feed_header = wait.until(EC.visibility_of_element_located(MainPageLocators.BUTTON_ORDER_FEED))
            assert order_feed_header.is_displayed()

        with allure.step('Переход в раздел "Конструктор"'):
            constructor_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_CONSTRUCTOR))
            constructor_btn.click()

        with allure.step('Проверка открытия раздела "Конструктор"'):
            constructor_title = wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
            assert constructor_title.is_displayed(), "Раздел 'Конструктор' не открылся"


    @allure.title('Проверка открытия окна с деталями ингредиентов при клике на ингредиент')
    @pytest.mark.parametrize('ingredient_locator', [
        MainPageLocators.BUN_2,
        MainPageLocators.INGREDIENT_SAUCES_X
    ])
    def test_ingredient_details_window_opening(self, driver, ingredient_locator):
        wait = WebDriverWait(driver, 10)

        with allure.step(f'Ожидание и клик по ингредиенту с локатором {ingredient_locator}'):
            ingredient = wait.until(EC.element_to_be_clickable(ingredient_locator))
            ingredient.click()

        with allure.step('Проверка открытия окна с деталями ингредиента'):
            ingredient_details = wait.until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))
            assert ingredient_details.is_displayed(), "Окно с деталями ингредиента не открылось"

        with allure.step('Закрытие окна с деталями ингредиента'):
            close_button = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_CLOSE_CONFIRMATION))
            close_button.click()

        with allure.step('Проверка закрытия окна с деталями ингредиента'):
            wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))


    @allure.title('Проверка закрытия окна с деталями ингредиентов кликом на крестик')
    def test_ingredient_details_window_closing(self, driver):
        wait = WebDriverWait(driver, 10)

        with allure.step('Ожидание и клик по ингредиенту "Краторная булка N-200i"'):
            ingredient = wait.until(EC.element_to_be_clickable(MainPageLocators.BUN_2))
            ingredient.click()

        with allure.step('Проверка открытия окна с деталями ингредиента'):
            ingredient_details = wait.until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))
            assert ingredient_details.is_displayed(), "Окно с деталями ингредиента не открылось"

        with allure.step('Закрытие окна с деталями ингредиента'):
            close_button = wait.until(EC.element_to_be_clickable(MainPageLocators.BUTTON_CLOSE_CONFIRMATION))
            close_button.click()

        with allure.step('Проверка закрытия окна с деталями ингредиента'):
            closed = wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))
            assert closed, "Окно с деталями ингредиента не закрылось"


    @allure.title("Проверка увеличения числа на счетчике ингредиента при добавлении в заказ ингредиента")
    def test_increase_number_on_ingredient(self, driver):
        wait = WebDriverWait(driver, 10)

        with allure.step("Ожидание видимости элемента BUN_1"):
            ingredient = wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_1))

        # Получаем начальное значение счётчика с помощью метода класса
            initial_counter_value = int(self.get_number_of_ingredients_in_counter())

        with allure.step("Перетаскивание ингредиента в корзину"):
            self.drag_and_drop_ingredient_to_order()

        with allure.step("Проверяем увеличение значения счётчика"):
            wait.until(EC.text_to_be_present_in_element(
                MainPageLocators.INGREDIENT_COUNTER_BUN, str(initial_counter_value + 1)
            ))

            updated_counter_value = int(self.get_number_of_ingredients_in_counter())
            assert updated_counter_value > initial_counter_value, \
                f"Счётчик не увеличился! Текущее значение: {updated_counter_value}, ожидалось больше {initial_counter_value}"
