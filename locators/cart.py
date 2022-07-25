from selene.support.shared import browser

total_price_text = browser.element('//h3[@id="totalp"]')
all_devices_in_cart = browser.elements('//tbody/tr')
place_order_button = browser.element('//button[contains(text(),"Place Order")]')
