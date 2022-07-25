from selene.support.shared import browser

add_to_cart_button = browser.element('//a[contains(text(),"Add to cart")]')
device_price_container = browser.element('//*[@id="tbodyid"]/h3')
product_added_alert_message = 'Product added.'
