import re
from selenium.common.exceptions import NoSuchElementException
from homework_Selenium.locators.catalog_page_locators import CatalogPageLocators
from homework_Selenium.pages.base_page import BasePage


class CatalogPage(BasePage):

    def is_sort_by_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SORT_BY_INPUT) is not None

    def is_show_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.SHOW_INPUT) is not None

    def is_list_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.LIST_VIEW_BUTTON) is not None

    def is_grid_view_input_present(self):
        assert self.wait_for_element(CatalogPageLocators.GRID_VIEW_BUTTON) is not None

    def is_side_menu_present(self):
        assert self.wait_for_element(CatalogPageLocators.SIDE_MENU) is not None

    def get_item_with_num(self, item_num):
        items = self.wait_for_elements(CatalogPageLocators.PRODUCT_THUMB)
        try:
            item = items[item_num]
        except IndexError:
            raise NoSuchElementException(f"No itme with number {item_num}")
        return item

    def get_item_price(self, item_num=0):
        item = self.get_item_with_num(item_num)
        price = item.find_element(*CatalogPageLocators.PRICE)
        price_elements = price.split()
        return price_elements[0]

    def add_item_to_cart(self, item_num=0):
        item = self.get_item_with_num(item_num)
        add_button = item.find_element(*CatalogPageLocators.ADD_TO_CART_ICON)
        add_button.click()

    def add_item_to_compare(self, item_num=0):
        item = self.get_item_with_num(item_num)
        compare_button = item.find_element(*CatalogPageLocators.COMPARE_ICON)
        compare_button.click()

    def add_item_to_fav(self, item_num=0):
        item = self.get_item_with_num(item_num)
        fav_button = item.find_element(*CatalogPageLocators.ADD_TO_FAV_ICON)
        fav_button.click()

    def get_product_compare_num(self):
        compare_link_text = self.wait_for_element(CatalogPageLocators.PRODUCT_COMPARE_LINK).text
        res = re.search(r"(\d{1,})", compare_link_text)
        return int(res.group(0))

    def is_compare_num_equal_to(self, num):
        assert self.get_product_compare_num() == num
