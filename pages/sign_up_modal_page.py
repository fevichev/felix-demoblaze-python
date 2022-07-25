from time import sleep

from hamcrest import assert_that, equal_to
from selene.support.conditions import be

from locators.sign_up_modal import alert_message, username_text_box, sign_up_button_modal, password_text_box
from utils.helper import get_text_of_alert


def populate_username_and_password(username, password):
    username_text_box.should(be.visible).set_value(username)
    password_text_box.should(be.clickable).set_value(password)
    sign_up_button_modal.click()


def verify_alert_message():
    sleep(1)
    actual_text_of_alert = get_text_of_alert()
    assert_that(actual_text_of_alert, equal_to(alert_message))
