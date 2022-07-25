from time import sleep

from busypie import wait, SECOND
from selene.support.shared import browser
from selenium.webdriver.support.expected_conditions import alert_is_present


def accept_alert_message():
    wait().at_most(4, SECOND).until(alert_is_present)
    browser.driver.switch_to.alert.accept()


def get_text_of_alert():
    return browser.driver.switch_to.alert.text


def json_extract(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
