import time

from lokators.main_page_locators import MainPageLocators
import pytest
import allure
from pages.main_page import MainPage
from seletools.actions import drag_and_drop
from pages.histori_page import FeedPage
from pages.auth_page import AuthPage


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
    def test_changes_counter_for_quantity_of_orders_all_time(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.main_page_loading_wait()  # ждём загрузку и скрытие оверлея
        main_page.get_text_on_title_collest_burger()#ожидаем заголовок Собирите бургер
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_initial = feed_page.get_quantity_of_orders()  # Получаем текущее значение счетчика "Выполнено за всё время"
        main_page.click_on_button_constructor()# Переход в конструктор
        main_page.click_on_button_make_order()  # клик создания заказа
        main_page.drag_and_drop_ingredient_to_order()# добавляем ингред
        main_page.check_displaying_of_confirmation_window_of_order()  # отображение окна о создании заказа
        main_page.wait_for_loading_animation_hide()  # ждем загрузки анимации
        main_page.get_number_of_order_in_window_confirmation()# получаем номер заказа в окне
        main_page.click_on_button_close_confirmation_window()  # закрыть окно
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_modified = feed_page.get_quantity_of_orders()
        assert orders_initial in orders_modified


    @allure.title('Проверка увеличения числа на счетчике «Выполнено за СЕГОДНЯ» на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders_for_todey(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.main_page_loading_wait()  # ждём загрузку и скрытие оверлея
        main_page.get_text_on_title_collest_burger()# ожидаем заголовок "Собирите бургер"
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_initial = feed_page.get_daily_quantity_of_orders()  # Получаем текущее значение счетчика "за СЕГОДНЯ"
        main_page.click_on_button_constructor()# Переход в конструктор
        main_page.click_on_button_make_order()  # клик создания заказа
        main_page.drag_and_drop_ingredient_to_order()# добавляем ингред
        main_page.check_displaying_of_confirmation_window_of_order()  # отображение окна о создании заказа
        main_page.wait_for_loading_animation_hide()  # ждем загрузки анимации
        main_page.get_number_of_order_in_window_confirmation()# получаем номер заказа в окне
        main_page.click_on_button_close_confirmation_window()  # закрыть окно
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_modified = feed_page.get_daily_quantity_of_orders()
        assert orders_initial in orders_modified
        #print(f"Номер заказа1: {orders_initial}")  # выводим номер на экран
        #print(f"Номер заказа2: {orders_modified}")  # выводим номер на экран


    @allure.title('После оформления заказа его номер появляется в разделе "В работе" на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders_for_todey(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.main_page_loading_wait()  # ждём загрузку и скрытие оверлея
        main_page.get_text_on_title_collest_burger()# ожидаем заголовок "Собирите бургер"
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_initial = feed_page.get_daily_quantity_of_orders()  # Получаем текущее значение счетчика "за СЕГОДНЯ"
        main_page.click_on_button_constructor()# Переход в конструктор
        main_page.click_on_button_make_order()  # клик создания заказа
        main_page.drag_and_drop_ingredient_to_order()# добавляем ингред
        main_page.check_displaying_of_confirmation_window_of_order()  # отображение окна о создании заказа
        main_page.wait_for_loading_animation_hide()  # ждем загрузки анимации
        main_page.get_number_of_order_in_window_confirmation()# получаем номер заказа в окне
        main_page.click_on_button_close_confirmation_window()  # закрыть окно
        main_page.click_header_button_order_feed()  # лента заказов переход
        orders_modified = feed_page.get_daily_quantity_of_orders()
        assert orders_initial in orders_modified
        #print(f"Номер заказа1: {orders_initial}")  # выводим номер на экран
        #print(f"Номер заказа2: {orders_modified}")  # выводим номер на экран


    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_in_progress_section(self, driver, login):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page.main_page_loading_wait()  # ожидаем исчезновения оверлея
        constructor_page.wait_for_header_make_burger()  # ожидаем заголовок Соберите бургер
        constructor_page.create_order()  # создаем заказ
        order_feed_page.wait_header_id_order()  # ожидаем заголовок всплывающего окна с номером заказа
        order_number = order_feed_page.get_order_number()  # получаем номер заказа в окне
        order_feed_page.wait_for_loading_animation_end()  # ждем загрузки анимации
        order_feed_page.scroll_to_x_on_popup_and_close()  # закрываем всплывающее окно с номером id заказа
        order_feed_page.wait_button_order_feed()  # ожидаем появления кнопки Лента заказов
        order_feed_page.click_button_order_feed()  # переходим в раздел Лента Заказов
        order_feed_page.wait_header_order_feed()  # ожидаем появления заголовка Лента заказов
        actual_number = order_feed_page.get_all_order_numbers_feed()  # получаем список всех номеров в разделе В работе
        assert order_number in actual_number  # сравниваем результат



        #orders_count_1 = feed_page.get_quantity_of_orders() # Получаем текущее значение счетчика "Выполнено за всё время"
        #count_before = int(orders_count_1)
        # Возвращаемся на главную, добавляем ингредиент в корзину и оформляем заказ
        #main_page.click_on_button_constructor()# Переход в конструктор
        #main_page.drag_and_drop_ingredient_to_order()# добавляем ингред
        #main_page.click_on_button_make_order()# клик создания заказа

        #main_page.click_on_button_close_confirmation_window()# закрыть окно
        #main_page.click_header_button_order_feed()# лента заказов переход
        #orders_count_2 = feed_page.get_quantity_of_orders()
        #assert orders_count_1 < orders_count_2

