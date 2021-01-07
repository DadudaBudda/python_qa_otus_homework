from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    USERNAME_INPUT = By.CSS_SELECTOR, "[name='username']"
    PASSWORD_INPUT = By.CSS_SELECTOR, "[name='password']"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), ' Login')]"
    FORGOTTEN_PASSWORD_LINK = By.CSS_SELECTOR, ".help-block a"
    HEADER_LOGO = By.CSS_SELECTOR, "#header-logo"
