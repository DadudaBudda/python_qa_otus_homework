from homework_Selenium.pages.login_page import LoginPage as login_page


def test_is_new_customer_section_present(driver, login):
    login_page().is_new_customer_section_present()


def test_is_returning_customer_section_present(driver, login):
    login_page().is_returning_customer_section_present()


def test_is_email_input_present(driver, login):
    login_page().is_email_input_present()


def test_is_password_input_present(driver, login):
    login_page().is_password_input_present()


def test_is_login_button_present(driver, login):
    login_page().is_login_button_present()
