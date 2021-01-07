from selenium.webdriver.common.by import By
from homework_Selenium.locators.base_page_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    NEW_CUSTOMER_SECTION = By.XPATH, "//h2[contains(text(), 'New Customer')]/.."
    RETURNING_CUSTOMER_SECTION = By.XPATH, "//h2[contains(text(), 'Returning Customer')]/.."
    EMAIL_INPUT = By.XPATH, "//input[@name='email']"
    PASSWORD_INPUT = By.XPATH, "//input[@name='password']"
    LOGIN_BUTTON = By.XPATH, "//input[@value='Login']"
