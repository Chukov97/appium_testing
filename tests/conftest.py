import pytest
import allure
import allure_commons
# from settings import config
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
from appium import webdriver
from utils import attach_allure
from utils import file
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--environment", default='local')


def pytest_configure(config):
    environment = config.getoption("--environment")
    load_dotenv(dotenv_path=f'.env.{environment}')


@pytest.fixture
def environment(request):
    return request.config.getoption("--environment")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(environment):
    from settings import config
    # environment = request.config.getoption('--environment')
    # load_dotenv(dotenv_path=f'.env.{environment}')
    #
    options = config.driver_options(environment=environment)

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config.timeout = config.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach_allure.attach_screenshot()
    attach_allure.attach_xml()
    # session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

        # attach_allure.attach_bstack_video(session_id)

        # options = UiAutomator2Options().load_capabilities({
        #
        #     "platformName": "Android",
        #     "appium:deviceName": "Galaxy A22s",
        #     "appium:udid": "RZ8T10ZHCEM",
        #     "appium:automationName": "UiAutomator2",
        #     "appium:app": file.abs_path_from_project("app-alpha-universal-release.apk"),
        #     "appium:appWaitActivity": "org.wikipedia.*"
        #
        # })
    # elif platform == 'ios':
    #     options = XCUITestOptions().load_capabilities({
    #         "deviceName": "iPhone 11 Pro",
    #         "platformName": "ios",
    #         "platformVersion": "13",
    #
    #         "app": config.app,
    #
    #         'bstack:options': {
    #             "projectName": "First Python project",
    #             "buildName": "browserstack-build-1",
    #             "sessionName": "BStack first_test",
    #
    #             "userName": config.user_name,
    #             "accessKey": config.access_key
    #         }
    #     })
