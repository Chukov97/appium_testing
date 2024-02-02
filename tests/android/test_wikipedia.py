import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from screens.android.main_screen import main_screen
from screens.android.search_screen import search_screen


def test_search():
    with allure.step('Type search'):
        main_screen.click_search_form()
        main_screen.input_search_form('Appium')

    with allure.step('Verify content found'):
        results = search_screen.get_search_result()
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_search_result():
    with allure.step('Type search'):
        main_screen.click_search_form()
        main_screen.input_search_form('Appium')
    with allure.step('Open search result'):
        search_screen.open_search_result()
