from faker import Faker

from pages import home_page, sign_up_modal_page, login_modal_page, device_page, cart_page, place_order_modal_page
from utils import helper


class TestSignInPage:

    def test_sign_up(self, session):
        username = Faker().ascii_email()
        password = Faker().password()
        session['username'] = username
        session['password'] = password

        home_page.click_sign_up_button()
        sign_up_modal_page.populate_username_and_password(username, password)
        sign_up_modal_page.verify_alert_message()
        helper.accept_alert_message()

    def test_login(self, session):
        home_page.click_login_top_menu_button()
        login_modal_page.login_with_credentials(session['username'], session['password'])
        home_page.verify_user_is_logged_in(session)

    def test_add_to_cart(self):
        home_page.select_device_from_list('Nexus 6')
        device_page.move_device_to_cart()
        device_page.verify_device_was_added_to_cart()
        helper.accept_alert_message()
        home_page.click_top_logo()
        home_page.select_device_from_list('MacBook Pro')
        device_page.move_device_to_cart()
        device_page.verify_device_was_added_to_cart()
        helper.accept_alert_message()
        home_page.click_top_logo()

    def test_cart(self):
        home_page.click_cart_top_menu()
        cart_page.verify_cart_has_selected_devices()
        cart_page.verify_total_price()

    def test_place_order(self):
        cart_page.click_place_order_button()
        place_order_modal_page.populate_order_fields()
        place_order_modal_page.click_purchase_button()
        place_order_modal_page.verify_order_is_submitted()
        place_order_modal_page.verify_submitted_final_price()
        place_order_modal_page.click_ok_on_submission_modal()

    def test_login_api(self, session):
        home_page.click_top_logo()
        home_page.click_login_top_menu_button()
        login_modal_page.login_with_credentials(session.get("username"), session.get("password"))
        home_page.verify_user_is_logged_in(session)

    def test_add_device(self):
        home_page.select_device_from_list("Nexus 6")
        device_page.move_device_to_cart()
        device_page.verify_device_was_added_to_cart()
        helper.accept_alert_message()
        home_page.click_top_logo()

    def test_cart_with_api(self, session):
        home_page.click_cart_top_menu()
        cart_page.verify_number_of_items_in_the_card(1, session)
        cart_page.verify_price_of_the_selected_phone(650, session)
        cart_page.verify_title_of_the_selected_phone("Nexus 6", session)
        cart_page.verify_item_id(3, session)
