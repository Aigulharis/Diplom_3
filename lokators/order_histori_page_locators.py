from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # Раздел "Выполнено за всё время"
    COMPLETED_IN_ALL_TIME = (By.XPATH, ".//div[contains(@class, 'mb-15') and .//p[text()='Выполнено за все время:']]")

    # Раздел "Выполнено за сегодня"
    COMPLETED_TODAY = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")


    # Заголовок раздела "В работе"
    TITLE_AT_WORK = (By.XPATH, '//p[@class="text text_type_main-medium" and text()="В работе:"]')
    #  './/ul[contains(@class, "OrderFeed_orderListReady")]/li'

    # Номер в разделе "В работе"
    AT_WORK = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady') and contains(@class, 'OrderFeed_orderList')]")


    # Название карточки заказа в ленте заказов с названием булки
    #TITLE_CARD_ORDER = (By.XPATH, ".//*[contains(@class, 'OrderHistory_listItem')]//h2")

    # Номер заказа в списке в ленте заказов
    #ID_CARD_ORDER = (By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]")

    # Карточка заказа в списке с заказами
    #CARD_ORDER = (By.XPATH, ".//*[contains(@class, 'OrderHistory_listItem')]")





