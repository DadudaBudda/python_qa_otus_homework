import pytest
from selenium import webdriver as DRIVER
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions

ALL_TODOS = 200


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="permitted values: chrome, firefox, opera")
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="URL for test")


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
        driver = DRIVER.Firefox(options=firefox_options)

    elif browser == "opera":
        opera_options = OperaOptions()
        opera_options.add_argument("headless")
        driver = DRIVER.Opera(options=opera_options)

    else:
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        driver = DRIVER.Chrome(options=chrome_options, executable_path='../python_qa_otus_homework/chromedriver')

    driver.maximize_window()

    yield driver
    driver.quit()
