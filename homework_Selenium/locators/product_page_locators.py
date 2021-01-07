from selenium.webdriver.common.by import By
from homework_Selenium.locators.base_page_locators import BasePageLocators


class ProductPageLocators(BasePageLocators):
    THUMBNAILS_IMAGES = By.CSS_SELECTOR, "a.thumbnail>img"
    DESCRIPTION = By.CSS_SELECTOR, "div#tab-description"
    PRODUCT_INFO = By.CSS_SELECTOR, "div#product"
    ADD_TO_WISHLIST_BUTTON = By.CSS_SELECTOR, ".btn-group button>i.fa-heart"
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-cart"
    PRICE = By.CSS_SELECTOR, "li>h2"
    ITEM_NAME = By.CSS_SELECTOR, "#content h1"
    PREVIEW_IMAGE = By.CSS_SELECTOR, "figure>img"
