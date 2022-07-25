from selene.support.shared import browser

username_text_box = browser.element('#sign-username')
password_text_box = browser.element('#sign-password')
sign_up_button_modal = browser.element('//button[contains(text(),"Sign up")]')
alert_message = 'Sign up successful.'
