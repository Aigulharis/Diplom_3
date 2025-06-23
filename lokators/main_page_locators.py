from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Конструкторы"
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//a[p[text()='Конструктор']]")

    # Заголовок раздела "Конструктор"
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Заголовок раздела "Собери бургер"
    COLLECT_BURGER = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')

    # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED = (By.XPATH, ".//a[p/text()='Лента Заказов']")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка "Войти в аккаунт" на главной странице
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Булки']]")

    # Активная кнопка "Булки"
    ACTIVE_TAB_BUNS = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]")

    # Ингридиент - булка - Флюоресцентная булка R2 -D3
    BUN_1 = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']")

    # Ингридиент - булка - Краторная булка N-200i
    BUN_2 = (By.XPATH, ".//a/p[text()='Краторная булка N-200i']/ancestor::a")

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

    # Заголовок окна "Детали ингредиента"
    INGREDIENT_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Корзина
    BASKET = (By.XPATH, './/section[contains(@class, "BurgerConstructor_basket")]')

    # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')

    # Окно подтверждения создания заказа
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')
    # Номер заказа в окне подтверждения
    ORDER_ID_CONFIRMATION_WINDOW = (By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка-крестик закрывающая окно "Детали ингредиента"
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')

    # Счетчик ингредиента
    INGREDIENT_COUNTER_BUN = (By.XPATH, ".//div[contains(@class, 'counter_counter')]/p[contains(@class, 'counter_counter__num')]")
    #//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, 'counter')]")

    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    # Кнопка-крестик закрывающая окна подтверждения заказа
    BUTTON_CLOSE_ORDER = (By.XPATH, './/button/*[name()="svg"]/*[starts-with(@d,"M3.29289")]')


    #Кнопка логотипа "Stella Burgers@
    #LOGO_STELLA_BURGERS = (By.TAG_NAME, "svg")

