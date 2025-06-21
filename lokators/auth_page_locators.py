from selenium.webdriver.common.by import By


class AuthLocators:
    # 1. Вход в личный кабинет
    # 1.1. Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # 1.2. Поле ввода email +
    EMAIL_ACCOUNT = (By.XPATH, ".//input[@type='text']")

    # 1.3. Поле ввода пароля +
    PASSWORD_ACCOUNT = (By.XPATH, ".//input[@name = 'Пароль']")

    # 1.4. Кнопка "Войти" в личном кабинете
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
