from selenium.webdriver.common.by import By


class AdminDashboardPageLocators:
    USER_PROFILE = By.CSS_SELECTOR, "#user-profile"
    LOGOUT_BUTTON = By.CSS_SELECTOR, ".navbar-nav>li:nth-child(2)"
    CATALOG = By.CSS_SELECTOR, "#menu-catalog"
    PRODUCTS_IN_CATALOG = By.XPATH, "//li[@id='menu-catalog']/ul//*[contains(text(), 'Products')]"
    PRODUCTS_TABLE = By.CSS_SELECTOR, ".table-responsive"
