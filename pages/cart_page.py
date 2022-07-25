from time import sleep

from hamcrest import equal_to, assert_that, has_entries
from selene import query, be

from locators.cart import total_price_text, all_devices_in_cart, place_order_button
from pages.device_page import price_values
from rest import view_cart_api, view_device_description_api, delete_cart_api
from rest.view_cart_api import get_product_id


def verify_cart_has_selected_devices():
    sleep(1)
    assert_that(get_total_price(price_values), equal_to(int(total_price_text.get(query.text))))
    assert_that(all_devices_in_cart.get(query.size), equal_to(2))


def verify_total_price():
    expected_value_in_cart = {"Nexus 6": 650, "MacBook Pro": 1100}
    actual_values_in_cart = {}
    for row in all_devices_in_cart:
        device_name_in_cart = row.elements('td')[1].get(query.text)
        device_price_in_cart = int(row.elements('td')[2].get(query.text))
        actual_values_in_cart[device_name_in_cart] = device_price_in_cart

    assert_that(expected_value_in_cart, has_entries(actual_values_in_cart))


def click_place_order_button():
    place_order_button.should(be.visible).click()


def verify_number_of_items_in_the_card(expected_items_number, session):
    number_of_items_in_cart = view_cart_api.get_size_of_items_in_cart(session)
    assert_that(number_of_items_in_cart, equal_to(expected_items_number))


def verify_price_of_the_selected_phone(expected_item_price, session):
    price = view_device_description_api.get_price(session)
    assert_that(price, equal_to(expected_item_price))


def verify_title_of_the_selected_phone(expected_phone_title, session):
    device_name = view_device_description_api.get_title(session)
    assert_that(device_name, equal_to(expected_phone_title))


def verify_item_id(expected_id, session):
    assert_that(get_product_id(session), equal_to(expected_id))


def delete_all_cart_api(session):
    delete_cart_api.delete_cart_via_api(session.get("username"))


def get_total_price(prices):
    return sum(prices)
