import pytest
import os
from settings import config
from appium.options.ios import XCUITestOptions
from selene import browser

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",

        # Set URL of the application under test
        "app": config.app,

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = config.remote_url
    browser.config.driver_options = options
    browser.config.timeout = config.timeout

    yield

    browser.quit()
