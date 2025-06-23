import time

from lokators.main_page_locators import MainPageLocators
import pytest
import allure
from pages.main_page import MainPage
from seletools.actions import drag_and_drop
from pages.histori_page import FeedPage
from pages.base_page import BasePage

class TestCounter:

    @allure.title('Проверка увеличения числа на счетчике ингредиента при добавлении в заказ ингредиента')
    def test_increase_number_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()  # Ждём загрузку страницы и скрытие overlay
        counter_before = main_page.get_count_of_ingredients()
        # Перетаскиваем ингредиент в корзину
        main_page.drag_and_drop_ingredient_to_order()
        counter_after = main_page.get_count_of_ingredients()
        # Проверяем увеличение значения счетчика
        assert counter_before < counter_after


    @allure.title('Проверка увеличения числа на счетчике «Выполнено за всё время» на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders(self, driver, login):
        driver = login
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.main_page_loading_wait()  # ждём загрузку и скрытие оверлея
        # Переход на страницу "Лента заказов"
        main_page.click_header_button_order_feed()
        # Получаем текущее значение счетчика "Выполнено за всё время"
        orders_count_1 = feed_page.get_quantity_of_orders()
        #count_before = int(orders_count_1)
        # Возвращаемся на главную, добавляем ингредиент в корзину и оформляем заказ
        main_page.click_on_button_constructor()# Переход в конструктор
        main_page.drag_and_drop_ingredient_to_order()# добавляем ингред
        main_page.click_on_button_make_order()# клик создания заказа
        main_page.check_displaying_of_confirmation_window_of_order()#отображение окна
        main_page.click_on_button_close_confirmation_window()# закрыть окно
        main_page.click_header_button_order_feed()# лента заказов переход
        orders_count_2 = feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2


