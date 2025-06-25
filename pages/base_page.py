import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from data import global_timeout
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator, global_timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать изменения текста на элементе')
    def wait_for_element_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, value))

    #@allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    #def wait_for_attribute(self, locator, attribute, value, timeout=10):
    #    return WebDriverWait(self.driver, timeout).until(
    #        EC.text_to_be_present_in_element_attribute(locator, attribute, value)
    #    )

    @allure.step("Подождать пока элемент не станет невидимым")
    def wait_for_element_hide(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Проверить, что элемент стал невидимым")
    def check_element_hide(self, locator, timeout=15):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator, global_timeout=15):
        return self.wait_for_element(locator, global_timeout)

    @allure.step('Подождать изменения текста на элементе')
    def wait_for_element_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))







