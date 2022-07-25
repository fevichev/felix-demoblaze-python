import os

import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from definitions import browser_name, URL, gh_token


@pytest.fixture(scope='session', autouse=True)
def session():
    return {}


@pytest.fixture(scope='session', autouse=True)
def setup_browser():
    if browser_name.lower() == 'chrome':
        browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser_name.lower() == 'firefox':
        browser.config.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        os.environ['GH_TOKEN'] = gh_token

    browser.config.timeout = 3
    browser.config.driver.implicitly_wait(3)
    browser.config.driver.maximize_window()
    browser.config.driver.delete_all_cookies()
    browser.config.driver.timeouts.script = 3
    browser.config.driver.timeouts.page_load = 3
    browser.open(URL['UI'])
