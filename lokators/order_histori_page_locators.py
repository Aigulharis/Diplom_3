from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # Заголовок "Лента заказов"
    TITLE_ORDER_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]/h1")

    # Раздел "Выполнено за всё время"
    COMPLETED_IN_ALL_TIME = (By.XPATH, ".//div[contains(@class, 'mb-15') and .//p[text()='Выполнено за все время:']]")

    # Раздел "Выполнено за сегодня"
    COMPLETED_TODAY = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")

    # Заголовок раздела "В работе"
    TITLE_AT_WORK = (By.XPATH, '//p[@class="text text_type_main-medium" and text()="В работе:"]')

    # Номер заказа в разделе "В работе"
    AT_WORK = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")





