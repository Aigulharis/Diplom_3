from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # Раздел "Выполнено за всё время"
    COMPLETED_IN_ALL_TIME = (By.XPATH, ".//div[contains(@class, 'mb-15') and .//p[text()='Выполнено за все время:']]")

    # Раздел "Выполнено за сегодня"
    COMPLETED_TODAY = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")

    # Раздел "В работе"
    AT_WORK = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady') and contains(@class, 'OrderFeed_orderList')]")


    # Карточка заказа в списке с заказами
    CARD_ORDER = (By.XPATH, ".//*[contains(@class, 'OrderHistory_listItem')]")

    # Название карточки заказа в списке с заказами с названием булки
    TITLE_CARD_ORDER = (By.XPATH, ".//*[contains(@class, 'OrderHistory_listItem')]//h2")

    # Номер заказа в списке с заказами
    CARD_ORDER_ID = (By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]")




