import pytest
from settings import config
from appium.options.android import UiAutomator2Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({

        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        "app": config.app,

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })

    browser.config.driver_remote_url = config.remote_url
    browser.config.timeout = config.timeout
    browser.config.driver_options = options

    yield

    browser.quit()
