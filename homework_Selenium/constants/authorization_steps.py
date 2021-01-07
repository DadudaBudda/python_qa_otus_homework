from homework_Selenium.constants import constants
from homework_Selenium.constants.constants import urls


def authorization(website_name):
    constants.DRIVER.get(get_url_data(website_name=website_name))
    print('\n' + constants.DRIVER.current_url)


def get_url_data(website_name):
    return urls[website_name]
