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

    @allure.step('Получить НОМЕР ЗАКАЗА "в работе"')
    def get_order_number_in_feed_progress_section(self):
        self.find_element_with_wait(OrderFeedPageLocators.AT_WORK)
        return self.get_text_on_element(OrderFeedPageLocators.AT_WORK)


    #@allure.step('Получить номер заказа в разделе "В работе"')
    #def get_order_number_in_feed_progress_section(self):
    #    return self.get_text_on_element(OrderFeedPageLocators.AT_WORK)


    @allure.step('Получить текст заголовка "В работе')
    def get_text_on_title_at_work(self):
        return self.get_text_on_element(OrderFeedPageLocators.TITLE_AT_WORK)

    #@allure.step("Получить список номеров заказов в разделе В работе")
    #def get_orders_numbers_in_work(self):
        #container = self.wait_for_element(OrderFeedPageLocators.AT_WORK) # Ждём видимости контейнера "В работе"
        #мorders_elements = container.find_elements_by_tag_name('li')# Получаем все элементы заказов внутри контейнера (например, все <li>)
        #orders_numbers = [elem.text for elem in orders_elements if elem.text.strip()]# Получаем текст (номер) каждого заказа и возвращаем список
        #return orders_numbers

    #@allure.step('Получить текст заголовка раздела заказов "Выполнено за всё время"')
    #def get_text_on_title_of_orders_list(self):
        #return self.get_text_on_element(OrderFeedPageLocators.COMPLETED_IN_ALL_TIME)

    #@allure.step('Проверить наличие номера заказа в списке ленты')
    #def check_id_order_in_feed(self, order_id):
        #locator = OrderFeedPageLocators.id_order_card_in_feed_with_substitutions
        #locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        #self.find_element_with_wait(locator_with_order_id)
        #return self.check_displaying_of_element(locator_with_order_id)

    #@allure.step('Кликнуть по первому (последнему) заказу в ленте')
    #def click_on_order_card(self):
    #    self.wait_visibility_of_element(OrderFeedPageLocators.order_in_feed)
    #    self.click_on_element(OrderFeedPageLocators.order_in_feed)

    #@allure.step('Получить текст заголовка окна с деталями заказа')
    #def get_text_on_title_of_modal_order(self):
    #    return self.get_text_on_element(OrderFeedPageLocators.title_of_modal_order)


    #@allure.step('Проверить наличие номера заказа в списке ленты')
    #def check_id_order_in_feed(self, order_id):
        #    locator = OrderFeedPageLocators.id_order_card_in_feed_with_substitutions
        #   locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        # self.find_element_with_wait(locator_with_order_id)
    # return self.check_displaying_of_element(locator_with_order_id)