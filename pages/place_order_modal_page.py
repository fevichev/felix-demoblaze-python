from time import sleep

from faker import Faker
from hamcrest import assert_that, equal_to
from selene import query
from selene.support.conditions import be

from locators.place_order_modal import name_order_text_box, country_order_text_box, city_order_text_box, \
    credit_card_order_text_box, month_order_text_box, year_order_text_box, purchase_button, ok_order_submit_button, \
    thank_you_text, order_description_text
from pages.device_page import price_values


def populate_order_fields():
    name = Faker().ascii_free_email()
    country = Faker().country()
    city = Faker().city()
    credit_card = Faker().credit_card_number()
    month = Faker().month_name()
    year = Faker().city()

    name_order_text_box.set_value(name)
    country_order_text_box.set_value(country)
    city_order_text_box.set_value(city)
    credit_card_order_text_box.set_value(credit_card)
    month_order_text_box.set_value(month)
    year_order_text_box.set_value(year)


def click_purchase_button():
    purchase_button.should(be.visible).click()


def verify_order_is_submitted():
    assert_that(thank_you_text.should(be.visible))
    assert_that(ok_order_submit_button.should(be.visible))


def verify_submitted_final_price():
    summary_total_price = int(order_description_text.get(query.text).split('\n')[1].split(' ')[1])
    assert_that(get_expected_total_price(price_values), equal_to(summary_total_price))


def click_ok_on_submission_modal():
    sleep(1)
    ok_order_submit_button.should(be.visible).click()


def get_expected_total_price(prices):
    return sum(prices)
