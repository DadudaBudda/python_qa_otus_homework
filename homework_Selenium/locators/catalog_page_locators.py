from selenium.webdriver.common.by import By
from homework_Selenium.locators.base_page_locators import BasePageLocators


class CatalogPageLocators(BasePageLocators):
    SORT_BY_INPUT = By.CSS_SELECTOR, "#input-sort"
    SHOW_INPUT = By.CSS_SELECTOR, "#input-limit"
    LIST_VIEW_BUTTON = By.CSS_SELECTOR, "#list-view"
    GRID_VIEW_BUTTON = By.CSS_SELECTOR, "#grid-view"
    SIDE_MENU = By.CSS_SELECTOR, ".list-group"
    PRODUCT_THUMB = By.CSS_SELECTOR, ".product-thumb"
    PRODUCT_COMPARE_LINK = By.CSS_SELECTOR, "#compare-total"
    ADD_TO_CART_ICON = By.CSS_SELECTOR, ".fa-shopping-cart"
    ADD_TO_FAV_ICON = By.CSS_SELECTOR, ".fa-heart"
    PRODUCT_HEADER = By.CSS_SELECTOR, ".caption>h4"
    PRODUCT_DESCRIPTION = By.CSS_SELECTOR, ".caption>p"
    COMPARE_ICON = By.CSS_SELECTOR, ".fa-exchange"
    PRICE = By.CSS_SELECTOR, ".price"

