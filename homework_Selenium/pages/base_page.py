from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from homework_Selenium.constants import constants
from homework_Selenium.locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self):
        self.driver = constants.DRIVER

    def get_current_url(self):
        print("Checking if {} page is loaded.".format(self.driver.current_url))

    def get_title(self):
        return self.driver.title

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def are_elements_present(self, locator):
        try:
            self.driver.find_elements(*locator)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element(self, locator, timeout=10):
        try:
            el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException("Cannot find element {} {}".format(locator[0], locator[1]))
        return el

    def wait_for_elements(self, locator, timeout=10):
        try:
            els = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise NoSuchElementException("Cannot find elements {} {}".format(locator[0], locator[1]))
        return els

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            els = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException("Cannot find elements {} {}".format(locator[0], locator[1]))
        return els

    def is_top_menu_present(self):
        assert self.wait_for_element(BasePageLocators.TOP_MENU) is not None

    def is_search_input_present(self):
        assert self.wait_for_element(BasePageLocators.SEARCH_INPUT) is not None

    def is_search_button_present(self):
        assert self.wait_for_element(BasePageLocators.SEARCH_BUTTON) is not None

    def is_cart_button_present(self):
        assert self.wait_for_element(BasePageLocators.CART_BUTTON) is not None

    def is_navigation_bar_present(self):
        assert self.wait_for_element(BasePageLocators.NAVIGATION_BAR) is not None

    def is_footer_present(self):
        assert self.wait_for_element(BasePageLocators.FOOTER) is not None

    def get_cart_items_number(self):
        cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
        cart_items = cart_items_total.text.split(" - ")[0]
        return cart_items

    def get_cart_total(self):
        cart_items_total = self.wait_for_element(BasePageLocators.CART_TOTAL)
        cart_total = cart_items_total.text.split(" - ")[1]
        return cart_total

    def click_cart(self):
        self.wait_for_element(BasePageLocators.CART_BUTTON).click()

    def is_items_num_in_cart_equal_to(self, number):
        assert f"{number} item(s)" == self.get_cart_items_number()

    def is_cart_total_equal_to(self, sum):
        assert sum == self.get_cart_total()

    def is_alert_present(self):
        assert self.wait_for_element(BasePageLocators.ALERT_SUCCESS) is not None

    def get_alert_text(self):
        return self.wait_for_element(BasePageLocators.ALERT_SUCCESS).text

    def is_text_in_alert(self, text):
        assert text in self.get_alert_text()
