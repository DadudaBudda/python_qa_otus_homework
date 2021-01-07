from selenium.common.exceptions import NoSuchElementException
from homework_Selenium.locators.product_page_locators import ProductPageLocators
from homework_Selenium.pages.base_page import BasePage


class ProductPage(BasePage):

    def are_thumbnail_images_present(self):
        assert self.wait_for_elements(ProductPageLocators.THUMBNAILS_IMAGES) is not None

    def is_description_present(self):
        assert self.wait_for_element(ProductPageLocators.DESCRIPTION) is not None

    def is_product_info_present(self):
        assert self.wait_for_element(ProductPageLocators.PRODUCT_INFO) is not None

    def is_add_to_wishlist_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_WISHLIST_BUTTON) is not None

    def is_add_to_cart_button_present(self):
        assert self.wait_for_element(ProductPageLocators.ADD_TO_CART_BUTTON) is not None

    def add_to_cart(self):
        self.wait_for_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_price(self):
        return self.wait_for_element(ProductPageLocators.PRICE).text

    def get_item_name(self):
        return self.wait_for_element(ProductPageLocators.ITEM_NAME).text

    def is_preview_opened(self):
        assert self.wait_for_element(ProductPageLocators.PREVIEW_IMAGE) is not None

    def get_thumbnail_image(self, item_num=0):
        thumbnail_images = self.wait_for_elements(ProductPageLocators.THUMBNAILS_IMAGES)
        try:
            thumbnail_image = thumbnail_images[item_num]
        except IndexError:
            raise NoSuchElementException(f"No thumbnail image with number {item_num}")
        return thumbnail_image

    def click_thumbnail_image(self, item_num=0):
        thumbnail_image = self.get_thumbnail_image(item_num)
        thumbnail_image.click()
