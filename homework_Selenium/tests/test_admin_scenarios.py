from homework_Selenium.pages.admin_dashboard_page import AdminDashboardPage


def test_login_and_quit(driver, admin_page):
    admin_dashboard_page = AdminDashboardPage()
    admin_dashboard_page.click_login_button()
    admin_dashboard_page.is_user_profile_present()
    admin_dashboard_page.is_logout_button_present()
    admin_dashboard_page.click_logout()


def test_open_product_list(driver, admin_page):
    admin_dashboard_page = AdminDashboardPage()
    admin_dashboard_page.click_login_button()
    admin_dashboard_page.click_catalog()
    admin_dashboard_page.click_products_in_catalog()
    admin_dashboard_page.is_products_table_present()
