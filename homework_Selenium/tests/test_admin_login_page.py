from homework_Selenium.pages.admin_login_page import AdminLoginPage as admin_login_page


def test_is_username_input_present(driver, admin_page):
    admin_login_page().is_username_input_present()


def test_is_password_input_present(driver, admin_page):
    admin_login_page().is_password_input_present()


def test_is_login_button_present(driver, admin_page):
    admin_login_page().is_login_button_present()


def test_is_forgotten_password_link_present(driver, admin_page):
    admin_login_page().is_forgotten_password_link_present()


def test_is_header_logo_present(driver, admin_page):
    admin_login_page().is_header_logo_present()
