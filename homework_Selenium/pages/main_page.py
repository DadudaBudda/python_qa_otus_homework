from selenium.common.exceptions import NoSuchElementException
from homework_Selenium.locators.main_page_locators import MainPageLocators
from homework_Selenium.pages.base_page import BasePage


class MainPage(BasePage):
    def check_open_cart(self):
        assert self.wait_for_element(MainPageLocators.POWERED_BY_OPEN_CART) is not None

    def is_slideshow_present(self):
        assert self.wait_for_element(MainPageLocators.SLIDESHOW) is not None

    def is_featured_products_present(self):
        assert self.wait_for_element(MainPageLocators.FEATURED_PRODUCTS) is not None

    def is_brend_carousel_present(self):
        assert self.wait_for_element(MainPageLocators.BRENDS_CAROUSEL) is not None

    def get_item_with_num(self, item_num):
        featured_products = self.wait_for_elements(MainPageLocators.FEATURED_PRODUCTS)
        try:
            featured_product = featured_products[item_num]
        except IndexError:
            raise NoSuchElementException(f"No element with number {item_num}")
        return featured_product

    def add_featured_to_fav(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        featured_product.find_element(*MainPageLocators.FAV_ICON).click()

    def add_featured_to_cart(self, item_num=0):
        featured_product = self.get_item_with_num(item_num)
        featured_product.find_element(*MainPageLocators.ADD_TO_CART_ICON).click()
