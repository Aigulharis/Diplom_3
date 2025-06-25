import allure
from pages.histori_page import FeedPage
from pages.main_page import MainPage


class TestCheckingBasicFunctions:
    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    def test_going_feed_order(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step('Нажать на кнопку "Лента заказов" в шапке'):
            main_page.click_header_button_order_feed()
        with allure.step('Проверить заголовок на странице Ленты заказов'):
            assert feed_page.get_text_title_orders_list() == 'Лента заказов'


    @allure.title('Проверка перехода в раздел "Конструктор"')
    def test_going_constructor_section(self, driver):
        main_page = MainPage(driver)
        with allure.step('Нажать на блок "Лента заказов" в шапке'):
            main_page.click_header_button_order_feed()
        with allure.step('Нажать на блок "Конструктор"'):
            main_page.click_on_button_constructor()
        with allure.step('Проверить заголовок "Соберите бургер" на странице конструктора'):
            header_text = main_page.get_text_on_title_collest_burger()
            assert header_text, f"Ожидался заголовок 'Соберите бургер', но получен '{header_text}'"


    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_ingredient_details_window_opening(self, driver):
        main_page = MainPage(driver)
        with allure.step("Ожидание загрузки главной страницы без оверлея"):
            main_page.main_page_loading_wait()
        with allure.step("Клик по ингредиенту для открытия окна 'Детали ингредиента'"):
            main_page.click_on_ingredient()
        with allure.step("Проверка отображения окна 'Детали ингредиента'"):
            assert main_page.check_displaying_of_window_details(), "Окно с деталями ингредиента не открылось"


    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_ingredient_details_window_opening(self, driver):
        main_page = MainPage(driver)
        with allure.step("Ожидание загрузки главной страницы без оверлея"):
            main_page.main_page_loading_wait()
        with allure.step("Клик по ингредиенту для открытия окна 'Детали ингредиента"):
            main_page.click_on_ingredient()
        with allure.step("Закрытие окна 'Детали ингредиента'"):
            main_page.click_on_close_window()
        with allure.step("Ожидание загрузки главной страницы после закрытия окна без оверлея"):
            main_page.main_page_loading_wait()
        with allure.step("Проверка, что окно с деталями ингредиента закрылось"):
            assert not main_page.check_not_window_details(), "Окно с деталями ингредиента не закрылось"


    @allure.title('Проверка увеличения числа на счетчике ингредиента при добавлении в заказ ингредиента')
    def test_increase_number_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        with allure.step('Получение значения счетчика ингредиентов до добавления'):
            counter_before = main_page.get_count_of_ingredients()
        with allure.step('Добавляем ингредиенты в заказ'):
            main_page.drag_and_drop_ingredient_to_order()
        with allure.step('Получение значения счетчика ингредиентов после добавления'):
            counter_after = main_page.get_count_of_ingredients()
        with allure.step('Проверка, что счетчик увеличился'):
            assert counter_before < counter_after, "Счетчик ингредиентов не увеличился после добавления"


    @allure.title('Проверка увеличения числа на счетчике ингредиента при добавлении в заказ ингредиента')
    def test_increase_number_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        with allure.step('Получение значения счетчика ингредиентов до добавления'):
            counter_before = main_page.get_count_of_ingredients()
        with allure.step('Добавляем ингредиенты в заказ'):
            main_page.drag_and_drop_ingredient_to_order()
        with allure.step('Получение значения счетчика ингредиентов после добавления'):
            counter_after = main_page.get_count_of_ingredients()
        with allure.step('Проверка, что счетчик увеличился'):
            assert counter_before < counter_after, "Счетчик ингредиентов не увеличился после добавления"
