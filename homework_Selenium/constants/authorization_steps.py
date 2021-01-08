import allure

from homework_Selenium.constants import constants
from homework_Selenium.constants.constants import urls


def authorization(website_name):
    with allure.step(f'Авторизация на сайте {website_name}'):
        constants.DRIVER.get(get_url_data(website_name=website_name))


def get_url_data(website_name):
    return urls[website_name]
