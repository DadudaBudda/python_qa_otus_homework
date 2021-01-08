import json
import logging

import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from homework_Selenium.constants import constants, authorization_steps

logging.basicConfig(level=logging.INFO,
                    filename=f"homework_Selenium/tests/logs/selenium{time.strftime('%d-%m-%Y %H:%M')}.log")


class Listener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print('\nПопытка перехода на страницу {}'.format(url))

    def after_navigate_to(self, url, driver):
        print('Совершен переход на страницу {}'.format(url))

    def after_find(self, by, value, driver):
        print('Найден элемент By.{0} value:{1}'.format(by, value))

    def before_find(self, by, value, driver):
        print('Попытка найти элемент By.{0} value:{1}'.format(by, value))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--bversion", action="store", default="87.0")
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="URL for test")
    parser.addoption("--is_remote", action="store_true", default=False)
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="192.168.88.177")
    parser.addoption("--mobile", action="store_true")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def driver(request):
    logger = logging.getLogger('BrowserLogger')

    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    executor_url = f"http://{executor}:4444/wd/hub"
    mobile = request.config.getoption("--mobile")
    is_remote = request.config.getoption("--is_remote")

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "Tester",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs,
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    mobile_emulation = {"deviceName": "iPhone 5/SE"}

    if is_remote:

        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = mobile_emulation

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    else:
        if browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.headless = True
            driver = webdriver.Firefox(options=firefox_options)

        elif browser == "opera":
            opera_options = OperaOptions()
            opera_options.add_argument("headless")
            driver = webdriver.Opera(options=opera_options)

        elif browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("headless")

            if mobile:
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = webdriver.Chrome(executable_path='homework_Selenium/driver/chromedriver', options=chrome_options)

        else:
            raise ValueError(f"{browser} browser not supported")

    constants.DRIVER = driver
    logger.info(f"Browser {browser} closed")

    if not mobile:
        driver.maximize_window()

    logger.info(f"Browser {browser} started.")
    constants.DRIVER = EventFiringWebDriver(driver=driver, event_listener=Listener())

    # Attach browser data
    allure.attach(
        name=constants.DRIVER.session_id,
        body=json.dumps(constants.DRIVER.desired_capabilities),
        attachment_type=allure.attachment_type.JSON)

    # Add environment info to allure-report
    with open("homework_Selenium/environment.xml", "w+") as file:
        file.write(f"""<environment>
                    <parameter>
                        <key>Browser</key>
                        <value>{browser}</value>
                    </parameter>
                    <parameter>
                        <key>Browser.Version</key>
                        <value>{version}</value>
                    </parameter>
                    <parameter>
                        <key>Executor</key>
                        <value>{executor}</value>
                    </parameter>
                </environment>
                """)

    yield

    logger.info(f"Browser {browser} closed")
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
