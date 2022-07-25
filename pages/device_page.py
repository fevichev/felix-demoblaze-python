from time import sleep

from hamcrest import assert_that, equal_to
from selene import query

from locators.device import add_to_cart_button, device_price_container, product_added_alert_message
from utils import helper

price_values = []


def move_device_to_cart():
    price = device_price_container.get(query.text).split(" ")[0].replace('$', '')
    price_values.append(int(price))
    add_to_cart_button.click()


def verify_device_was_added_to_cart():
    sleep(1)
    assert_that(helper.get_text_of_alert(), equal_to(product_added_alert_message))
