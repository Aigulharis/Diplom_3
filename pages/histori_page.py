from pages.base_page import BasePage
from lokators.order_histori_page_locators import OrderFeedPageLocators
import allure


class FeedPage(BasePage):
    @allure.step('Получить количество заказов в разделе "Выполнено за всё время"')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedPageLocators.COMPLETED_IN_ALL_TIME)
        return self.get_text_on_element(OrderFeedPageLocators.COMPLETED_IN_ALL_TIME)

    @allure.step('Получить количество заказов в разделе "Выполнено за сегодня"')
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedPageLocators.COMPLETED_TODAY)
        return self.get_text_on_element(OrderFeedPageLocators.COMPLETED_TODAY)

    @allure.step('Получить номер заказа в разделе "В работе"')
    def get_order_number_in_feed_progress_section(self):
        return self.get_text_on_element(OrderFeedPageLocators.AT_WORK)

    @allure.step('Получить текст заголовка "В работе')
    def get_text_on_title_at_work(self):
        return self.get_text_on_element(OrderFeedPageLocators.TITLE_AT_WORK)

    @allure.step('Получить текст заголовка раздела "Лента заказов"')
    def get_text_title_orders_list(self):
        return self.get_text_on_element(OrderFeedPageLocators.TITLE_ORDER_FEED)
