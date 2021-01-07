from selenium.webdriver.common.by import By


class BasePageLocators:
    TOP_MENU = By.CSS_SELECTOR, "#top .container"
    SEARCH_INPUT = By.CSS_SELECTOR, "#search input"
    SEARCH_BUTTON = By.CSS_SELECTOR, "#search button"
    CART_BUTTON = By.CSS_SELECTOR, "#cart"
    ITEMS_IN_CART = By.CSS_SELECTOR, "table.table-striped"
    CART_TOTAL = By.CSS_SELECTOR, "#cart-total"
    NAVIGATION_BAR = By.CSS_SELECTOR, "ul.navbar-nav"
    FOOTER = By.CSS_SELECTOR, "footer"
    ALERT_SUCCESS = By.CSS_SELECTOR, ".alert-success"
