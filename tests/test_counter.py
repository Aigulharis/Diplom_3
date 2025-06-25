import time

from lokators.main_page_locators import MainPageLocators
import pytest
import allure
from pages.main_page import MainPage
from seletools.actions import drag_and_drop
from pages.histori_page import FeedPage
from pages.auth_page import AuthPage
import time


class TestCounter:

    @allure.title('Проверка увеличения числа на счетчике ингредиента при добавлении в заказ ингредиента')
    def test_increase_number_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()  # Ждём загрузку и скрытие невидимого окна (оверлея)
        with allure.step('Получение значения счетчика ингредиентов до добавления'):
            counter_before = main_page.get_count_of_ingredients()
        with allure.step('Добавляем ингредиенты в заказ'):
            main_page.drag_and_drop_ingredient_to_order()
        with allure.step('Получение значения счетчика ингредиентов после добавления'):
            counter_after = main_page.get_count_of_ingredients()
        with allure.step('Проверка, что счетчик увеличился'):
            assert counter_before < counter_after, "Счетчик ингредиентов не увеличился после добавления"

    @allure.title('Проверка увеличения числа на счетчике «Выполнено за всё время» на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders_all_time(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step('Ожидание загрузки главной страницы и проверка заголовка'):
            main_page.main_page_loading_wait()
            main_page.get_text_on_title_collest_burger()
        with allure.step('Переход на страницу "Лента заказов" и получение текущего значения счетчика'):
            main_page.click_header_button_order_feed()
            orders_initial = feed_page.get_quantity_of_orders()
        with allure.step('Переход в Конструктор и создание заказа'):
            main_page.click_on_button_constructor()
            main_page.drag_and_drop_ingredient_to_order()
            main_page.click_on_button_make_order()
        with allure.step('Ожидание появления окна подтверждения заказа и получение номера заказа'):
            main_page.check_displaying_of_confirmation_window_of_order()
            main_page.wait_for_loading_animation_hide()
            main_page.get_number_of_order_in_window_confirmation()
        with allure.step('Закрытие окна подтверждения заказа и возврат в "Ленту заказов"'):
            main_page.click_on_button_close_confirmation_window()
            main_page.click_header_button_order_feed()
        with allure.step('Проверка изменения значения счетчика заказов'):
            orders_modified = feed_page.get_quantity_of_orders()
            assert orders_initial < orders_modified, "Счетчик заказов не обновился после создания нового заказа"


    @allure.title('Проверка увеличения числа на счетчике «Выполнено за СЕГОДНЯ» на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders_for_today(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step('Ожидание загрузки главной страницы и проверка заголовка'):
            main_page.main_page_loading_wait()
            main_page.get_text_on_title_collest_burger()
        with allure.step('Переход на страницу "Лента заказов" и получение текущего значения счетчика за сегодня'):
            main_page.click_header_button_order_feed()
            orders_initial = feed_page.get_daily_quantity_of_orders()
        with allure.step('Переход в Конструктор и создание заказа'):
            main_page.click_on_button_constructor()
            main_page.drag_and_drop_ingredient_to_order()
            main_page.click_on_button_make_order()
        with allure.step('Ожидание появления окна подтверждения заказа и получение номера заказа'):
            main_page.check_displaying_of_confirmation_window_of_order()
            main_page.wait_for_loading_animation_hide()
            main_page.get_number_of_order_in_window_confirmation()
        with allure.step('Закрытие окна подтверждения заказа и возврат в "Ленту заказов"'):
            main_page.click_on_button_close_confirmation_window()
            main_page.click_header_button_order_feed()
        with allure.step('Проверка изменения счетчика заказов за сегодня'):
            feed_page.get_text_on_title_at_work()
            orders_modified = feed_page.get_daily_quantity_of_orders()
            assert orders_initial < orders_modified, "Счетчик заказов за сегодня не обновился после создания нового заказа"

    @allure.title('После оформления заказа его номер появляется в разделе "В работе" на странице "Лента заказов"')
    def test_changes_counter_for_quantity_of_orders_in_work(self, driver, login):
        driver = login  # фикстура
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step('Ожидание загрузки главной страницы и проверка заголовка'):
            main_page.main_page_loading_wait()  # Ждём загрузку и скрытие (невидимого окна) оверлея
            main_page.get_text_on_title_collest_burger()  # На главной странице ожидаем заголовок "Собирите бургер"
        with allure.step('Создание заказа и добавление ингредиентов'):
            main_page.click_on_button_make_order()  # Создаем заказ
            main_page.drag_and_drop_ingredient_to_order()  # Добавляем ингредиенты
        with allure.step('Появление окна подтверждения создания заказа и ожидание завершения загрузки'):
            main_page.check_displaying_of_confirmation_window_of_order()  # Отображение окна о создании заказа
            main_page.wait_for_loading_animation_hide()  # Ждем когда уйдет анимация загрузки заказа
        with allure.step('Получение номера заказа и закрытие окна подтверждения'):
            order_number = main_page.get_number_of_order_in_window_confirmation()  # Получаем номер заказа в окне подтверждения
            main_page.click_on_button_close_confirmation_window()  # Закрываем окно с номером заказа
        with allure.step('Переход на страницу "Лента заказов" и ожидание заголовка "В работе"'):
            main_page.click_header_button_order_feed()  # Переходим на страницу "Лента заказов"
            feed_page.get_text_on_title_at_work()  # ожидаем появления заголовка "В работе"
        with allure.step('Проверка наличия номера заказа в разделе "В работе"'):
            orders_in_work = feed_page.get_order_number_in_feed_progress_section()  # Получаем список номеров в разделе "В работе"
            #assert order_number in orders_in_work, f"Номер заказа {order_number} не найден в разделе 'В работе'"
            assert order_number.get_number_of_order_in_window_confirmation(orders_in_work), \
                f"Номер заказа {order_number} не появился в разделе 'В работе'"


