from lokators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть по кнопке перехода в личный кабинет')
    def click_on_personal_account_in_header(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть по кнопке Лента заказов')
    def click_header_button_order_feed(self):
        self.wait_for_element(MainPageLocators.BUTTON_ORDER_FEED)
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.wait_for_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Получение главного заголовка конструктора')
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
        return self.wait_for_attribute(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Закрыть окно "Детали ингредиента" окна о создании окна')
    def click_on_close_window(self):
        self.wait_for_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)


    @allure.step('Перетащить ингредиент в корзину')
    def drag_and_drop_ingredient_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.BUN_1)  # ингредиент
        target = self.find_element_with_wait(MainPageLocators.BASKET)  # корзина
        self.drag_and_drop_element(source, target)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_window_of_order(self):
        self.wait_for_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW)
        return self.wait_for_attribute(MainPageLocators.ORDER_CONFIRMATION_WINDOW)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_window_confirmation(self):
        self.wait_for_attribute(MainPageLocators.ORDER_ID_CONFIRMATION_WINDOW, '9999')
        return self.get_text_on_element(MainPageLocators.ORDER_ID_CONFIRMATION_WINDOW)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER_BUN)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_window_details(self):
        self.wait_for_element_hide(MainPageLocators.INGREDIENT_DETAILS)
        if not self.check_displaying_of_element(MainPageLocators.INGREDIENT_DETAILS):
            return True

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_window(self):
        self.check_displaying_of_element(MainPageLocators.BUTTON_CLOSE_ORDER)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_ORDER)


    # возможно не надо будет
    #@allure.step('Получить количество ингредиентов')
    #def get_count_of_ingredients(self):
    #    return self.get_text_on_element(MainPageLocators.count_of_ingredient)

    #def wait_visibility_of_element(self, PERSONAL_ACCOUNT_BUTTON):
    #    pass

    #@allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    #def check_not_displaying_of_window_details(self):
        #    self.wait_for_closing_of_element(MainPageLocators.header_of_modal_details)
        #if not self.check_displaying_of_element(MainPageLocators.header_of_modal_details):
    #   return True


    #@allure.step('Получить количество ингредиентов в счетчике')
    #def get_number_of_ingredients_in_counter(self):
        #    self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER_BUN)
    #    return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER_BUN)