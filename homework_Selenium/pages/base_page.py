import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from homework_Selenium.constants import constants
from homework_Selenium.locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self):
        self.driver = constants.DRIVER

    def get_title(self):
        return self.driver.title

    def get_element(self, locator):
        with allure.step(f'Найден элемент {locator}'):
            return self.driver.find_element(*locator)

    def get_elements(self, locator):
        with allure.step(f'Найден элементы {locator}'):
            return self.driver.find_elements(*locator)

    def is_element_present(self, locator):
        with allure.step(f'Показан элемент {locator}'):

            try:
                self.driver.find_element(*locator)
            except NoSuchElementException:
                return False
            return True

    def is_not_element_present(self, locator, timeout=3):
        with allure.step(f'Не показан элемент {locator}'):

            try:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                return True
            return False

    def are_elements_present(self, locator):
        with allure.step(f'Не показан элементы {locator}'):

            try:
                self.driver.find_elements(*locator)
            except NoSuchElementException:
                return False
            return True

    def wait_for_element(self, locator, timeout=10):
        with allure.step(f'Ожидание элемента {locator}'):
            try:
                el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                raise NoSuchElementException("Cannot find element {} {}".format(locator[0], locator[1]))
            return el

    def wait_for_elements(self, locator, timeout=10):
        with allure.step(f'Ожидание элементов {locator}'):
            try:
                els = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            except TimeoutException:
                raise NoSuchElementException("Cannot find elements {} {}".format(locator[0], locator[1]))
            return els

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        with allure.step(f'Ожидание видимости элемента {locator}'):
            try:
                els = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                raise NoSuchElementException("Cannot find elements {} {}".format(locator[0], locator[1]))
            return els

    def is_top_menu_present(self):
        with allure.step(f'is_top_menu_present'):
            assert self.wait_for_element(BasePageLocators.TOP_MENU) is not None

    def is_search_input_present(self):
        with allure.step(f'is_search_input_present'):
            assert self.wait_for_element(BasePageLocators.SEARCH_INPUT) is not None

    def is_search_button_present(self):
        with allure.step(f'is_search_button_present'):
            assert self.wait_for_element(BasePageLocators.SEARCH_BUTTON) is not None

    def is_cart_button_present(self):
        with allure.step(f'is_cart_button_present'):
            assert self.wait_for_element(BasePageLocators.CART_BUTTON) is not None

    def is_navigation_bar_present(self):
        with allure.step(f'is_navigation_bar_present'):
            assert self.wait_for_element(BasePageLocators.NAVIGATION_BAR) is not None

    def is_footer_present(self):
        with allure.step(f'is_footer_present'):
            assert self.wait_for_element(BasePageLocators.FOOTER) is not None

    def get_cart_items_number(self):
        with allure.step(f'get_cart_items_number'):
            cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
            cart_items = cart_items_total.text.split(" - ")[0]
            return cart_items

    def get_cart_total(self):
        with allure.step(f'get_cart_total'):
            cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
            cart_total = cart_items_total.text.split(" - ")[1]
            return cart_total

    def click_cart(self):
        with allure.step(f'click_cart'):
            self.wait_for_element(BasePageLocators.CART_BUTTON).click()

    def is_items_num_in_cart_equal_to(self, number):
        with allure.step(f'is_items_num_in_cart_equal_to {number}'):
            assert f"{number} item(s)" == self.get_cart_items_number()

    def is_cart_total_equal_to(self, sum):
        with allure.step(f'is_cart_total_equal_to'):
            assert sum == self.get_cart_total()

    def is_alert_present(self):
        with allure.step(f'Показан аллерт'):
            assert self.wait_for_element(BasePageLocators.ALERT_SUCCESS) is not None

    def get_alert_text(self):
        with allure.step(f'Текст аллерта {self.get_alert_text()}'):
            return self.wait_for_element(BasePageLocators.ALERT_SUCCESS).text

    def is_text_in_alert(self, text):
        with allure.step(f'Текст аллерта ожидаемы {text} и фактический{self.get_alert_text()}'):
            assert text in self.get_alert_text()
