import allure
from lokators.auth_page_locators import AuthLocators
from pages.base_page import BasePage
from lokators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(BasePage):

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.click_on_element(AuthLocators.ENTER_ACCOUNT_BUTTON)
        self.send_keys_to_input(AuthLocators.EMAIL, email)
        self.send_keys_to_input(AuthLocators.PASSWORD, password)
        self.click_on_element(AuthLocators.LOGIN_BUTTON)

