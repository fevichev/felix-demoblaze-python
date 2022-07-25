from locators.login_modal import login_username_text_box, login_password_text_box, login_button


def login_with_credentials(username, password):
    login_username_text_box.set_value(username)
    login_password_text_box.set_value(password)
    login_button.click()
