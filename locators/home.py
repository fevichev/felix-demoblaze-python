from selene.support.shared import browser

sign_up_button = browser.element('//*[@id="signin2"]')
login_top_menu_button = browser.element('//*[@id="login2"]')
logout_top_menu_button = browser.element("//a[@id='logout2']")
name_of_user = browser.element('//a[@id="nameofuser"]')
next_page_button = browser.element('//button[@id="next2"]')
main_logo_button = browser.element('//a[@id="nava"]')
cart_top_menu_button = browser.element('//a[contains(text(),"Cart")]')


def device_with_name(device_name):
    return browser.element(f'//a[contains(text(),"{device_name}")]')
