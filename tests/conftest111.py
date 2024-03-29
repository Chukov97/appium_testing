# import pytest
# import allure
# import allure_commons
# from settings import config
# from appium.options.android import UiAutomator2Options
# from appium.options.ios import XCUITestOptions
# from selene import browser, support
# from appium import webdriver
# from utils import attach_allure
#
#
# def pytest_addoption(parser):
#     parser.addoption("--platform", default='android')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def mobile_management(request):
#     platform = request.config.getoption('--platform')
#     if platform == 'android':
#         options = UiAutomator2Options().load_capabilities({
#
#             "platformVersion": "12.0",
#             "deviceName": "Samsung Galaxy S22 Ultra",
#
#             "app": config.app,
#
#             'bstack:options': {
#                 "projectName": "First Python project",
#                 "buildName": "browserstack-build-1",
#                 "sessionName": "BStack first_test",
#
#                 "userName": config.user_name,
#                 "accessKey": config.access_key
#             }
#         })
#     elif platform == 'ios':
#         options = XCUITestOptions().load_capabilities({
#             "deviceName": "iPhone 11 Pro",
#             "platformName": "ios",
#             "platformVersion": "13",
#
#             "app": config.app,
#
#             'bstack:options': {
#                 "projectName": "First Python project",
#                 "buildName": "browserstack-build-1",
#                 "sessionName": "BStack first_test",
#
#                 "userName": config.user_name,
#                 "accessKey": config.access_key
#             }
#         })
#
#     with allure.step('Init app session'):
#         browser.config.driver = webdriver.Remote(
#             config.remote_url,
#             options=options
#         )
#
#     browser.config.timeout = config.timeout
#     browser.config._wait_decorator = support._logging.wait_with(
#         context=allure_commons._allure.StepContext
#     )
#
#     yield
#
#     attach_allure.attach_screenshot()
#     attach_allure.attach_xml()
#     session_id = browser.driver.session_id
#
#     with allure.step('Tear down app session'):
#         browser.quit()
#
#     attach_allure.attach_bstack_video(session_id)
