from selenium.webdriver.common.by import By


class AuthLocators:

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка "Войти в аккаунт"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Кнопка "Войти" в личном кабинете
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Поле ввода email +
    EMAIL = (By.XPATH, ".//input[@type='text']")

    # Поле ввода пароля +
    PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")

    # Кнопка "Выйти" в личном кабинете
    #EXIT_BUTTON = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']//button[text()= 'Выход']")

