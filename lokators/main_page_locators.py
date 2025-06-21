from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Конструкторы"
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//a[p[text()='Конструктор']]")

    # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED = (By.XPATH, ".//a[p/text()='Лента Заказов']")

    # Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Булки']]")

    # Активная кнопка "Булки"
    ACTIVE_TAB_BUNS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]")

    # Ингридиент - булка - Флюоресцентная булка R2 -D3
    Bun_1 = (By.XPATH, ".//div[contains(@class, 'BurgerIngredient_ingredient__priceBox')]")

    # Ингридиент - булка - Краторная булка N-200i
    Bun_2 = (By.XPATH, ".//a/p[text()='Краторная булка N-200i']/ancestor::a")

    # Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")

    # Активная кнопка "Соусы"
    ACTIVE_TAB_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Соусы']]")

    # Ингридиент соус - Соус Spicy-X
    INGREDIENT_SAUCES_X = (By.XPATH, ".//a[p/text()='Соус Spicy-X']")

    # Ингридиент соус - Соус традиционный галактический
    INGREDIENT_SAUCES_Y = (By.XPATH, ".//a[p/text()='Соус традиционный галактический']")

    # Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")

    # Активная кнопка "Начинки"
    ACTIVE_TAB_FILLINGS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Начинки']]")

    # Ингридиент начинка - Биокотлета из марсианской Магнолии
    INGREDIENT_FILLINGS_1 = (By.XPATH, ".//a/p[text()='Биокотлета из марсианской Магнолии']/ancestor::a']")

    # Ингридиент начинка - Плоды Фалленианского дерева
    INGREDIENT_FILLINGS_2 = (By.XPATH, ".//a/p[text()='Плоды Фалленианского дерева']/ancestor::a']")

    # Корзина
    #BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.CLASS_NAME, 'button_button__33qZ0')

    # Окно подтверждения создания заказа
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')
    # Номер заказа в окне подтверждения
    ORDER_ID_CONFIRMATION_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка-крестик закрывающая окно подтвержденного заказа
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]')





    #Кнопка логотипа "Stella Burgers@
    #LOGO_STELLA_BURGERS = (By.TAG_NAME, "svg")

