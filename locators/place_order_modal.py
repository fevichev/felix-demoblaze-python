from selene.support.shared import browser

name_order_text_box = browser.element('//input[@id="name"]')
country_order_text_box = browser.element('//input[@id="country"]')
city_order_text_box = browser.element('//input[@id="city"]')
credit_card_order_text_box = browser.element('//input[@id="card"]')
month_order_text_box = browser.element('//input[@id="month"]')
year_order_text_box = browser.element('//input[@id="year"]')
purchase_button = browser.element('//button[contains(text(),"Purchase")]')
thank_you_text = browser.element('//h2[contains(text(),"Thank you for your purchase!")]')
ok_order_submit_button = browser.element('//button[contains(text(),"OK")]')
order_description_text = browser.element('//body/div[10]/p[1]')
