from selene.support.shared import browser

login_username_text_box = browser.element('//input[@id="loginusername"]')
login_password_text_box = browser.element('//input[@id="loginpassword"]')
login_button = browser.element('//button[contains(text(),"Log in")]')
