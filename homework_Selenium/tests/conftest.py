import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions

from homework_Selenium.constants import constants, authorization_steps


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="permitted values: chrome, firefox, opera"
    )
    parser.addoption(
        "--url", action="store", default="https://demo.opencart.com", help="URL for test"
    )


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def driver(browser):
    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("headless")
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()


    elif browser == "opera":
        opera_options = OperaOptions()
        opera_options.add_argument("headless")
        driver = webdriver.Opera(options=opera_options)
        driver.maximize_window()


    else:
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(executable_path='homework_Selenium/driver/chromedriver', options=chrome_options)
        driver.maximize_window()

    constants.DRIVER = driver

    yield
    if sys.exc_info():
        constants.DRIVER.quit()


@pytest.fixture()
def admin_page():
    authorization_steps.authorization(website_name='admin_login_page')


@pytest.fixture()
def catalog():
    authorization_steps.authorization(website_name='catalog_page')


@pytest.fixture()
def login():
    authorization_steps.authorization(website_name='login_page')


@pytest.fixture()
def main():
    authorization_steps.authorization(website_name='main_page')


@pytest.fixture()
def product():
    authorization_steps.authorization(website_name='product_page')
