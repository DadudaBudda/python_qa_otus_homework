from homework_Selenium.locators.admin_login_page_locators import AdminLoginPageLocators
from homework_Selenium.pages.base_page import BasePage


class AdminLoginPage(BasePage):

    def is_username_input_present(self):
        assert self.wait_for_elements(AdminLoginPageLocators.USERNAME_INPUT) is not None

    def is_password_input_present(self):
        assert self.wait_for_elements(AdminLoginPageLocators.PASSWORD_INPUT) is not None

    def is_login_button_present(self):
        assert self.wait_for_elements(AdminLoginPageLocators.LOGIN_BUTTON) is not None

    def is_forgotten_password_link_present(self):
        assert self.wait_for_elements(AdminLoginPageLocators.FORGOTTEN_PASSWORD_LINK) is not None

    def is_header_logo_present(self):
        assert self.wait_for_elements(AdminLoginPageLocators.HEADER_LOGO) is not None

    def input_username(self, username="demo"):
        username_input = self.wait_for_element(AdminLoginPageLocators.USERNAME_INPUT)
        if username_input:
            username_input.send_keys(username)

    def input_password(self, password="demo"):
        password_input = self.wait_for_element(AdminLoginPageLocators.PASSWORD_INPUT)
        if password_input:
            password_input.send_keys(password)

    def click_login_button(self):
        login_btn = self.wait_for_element(AdminLoginPageLocators.LOGIN_BUTTON)
        if login_btn:
            login_btn.click()
