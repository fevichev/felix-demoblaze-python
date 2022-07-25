from hamcrest import assert_that, ends_with
from selene import be, query
from selene.core.exceptions import TimeoutException

from locators.home import login_top_menu_button, sign_up_button, name_of_user, device_with_name, next_page_button, \
    main_logo_button, logout_top_menu_button, cart_top_menu_button


def click_sign_up_button():
    sign_up_button.should(be.visible).click()


def click_login_top_menu_button():
    login_top_menu_button.click()


def verify_user_is_logged_in(session):
    name_of_user.should(be.visible)
    assert_that(name_of_user.get(query.text), ends_with(session.get("username")))


def select_device_from_list(device_name):
    try:
        device_with_name(device_name).click()
    except TimeoutException:
        next_page_button.click()
        device_with_name(device_name).click()


def click_top_logo():
    main_logo_button.click()


def click_log_out():
    logout_top_menu_button.click()


def click_cart_top_menu():
    cart_top_menu_button.click()
