from lokators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть по кнопке перехода в "Личный кабинет"')
    def click_on_personal_account_in_header(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_header_button_order_feed(self):
        self.wait_for_element(MainPageLocators.BUTTON_ORDER_FEED)
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Переход на страницу Конструктора')
    def click_on_button_constructor(self):
        self.wait_for_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Получение заголовка Конструктор')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_account_button_in_main(self):
        self.click_on_element(MainPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_order_confirmation_window(self):
        self.wait_for_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW)
        return self.wait_for_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_for_element(MainPageLocators.BUN_1)
        self.click_on_element(MainPageLocators.BUN_1)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_window_details(self):
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS)
        return self.check_displaying_of_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Закрыть окно "Детали ингредиента"')
    def click_on_close_window(self):
        self.wait_for_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)

    @allure.step('Проверить закрытие окна "Детали ингредиента"')
    def check_not_window_details(self):
        self.wait_for_closing_element(MainPageLocators.INGREDIENT_DETAILS)
        if self.check_displaying_of_element(MainPageLocators.INGREDIENT_DETAILS):
            return False

    @allure.step('Перетащить ингредиент в корзину')
    def drag_and_drop_ingredient_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.BUN_1)  # ингредиент
        target = self.find_element_with_wait(MainPageLocators.BASKET)  # корзина
        self.drag_and_drop_element(source, target)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_on_button_make_order(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_window_of_order(self):
        return self.wait_for_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW)

    @allure.step('Обновление после Анимации в окне подтверждения заказа')
    def wait_for_loading_animation_hide(self):
        self.wait_for_element_hide(MainPageLocators.ANIMATION)

    @allure.step('Получить номер заказа (id) в окне о создании заказа')
    def get_number_of_order_in_window_confirmation(self):
        self.get_text_on_element(MainPageLocators.NUMBER_ORDER)
        return self.get_text_on_element(MainPageLocators.NUMBER_ORDER)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER_BUN)

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_window(self):
        self.check_displaying_of_element(MainPageLocators.BUTTON_CLOSE_ORDER)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_ORDER)

    @allure.step('Получить текст заголовка "Соберите бургер"')
    def get_text_on_title_collest_burger(self):
        return self.get_text_on_element(MainPageLocators.COLLECT_BURGER)

    @allure.step('Проверить отображение элемента крестик в окне о создании заказа')
    def check_displaying_of_element_button_close(self):
        self.check_displaying_of_element(MainPageLocators.BUTTON_CLOSE_ORDER)

