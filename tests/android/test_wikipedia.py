import allure
from selene import have
from screens.android.main_screen import main_screen
from screens.android.search_screen import search_screen
from screens.android.start_screen import start_screen


def test_search_appium(environment):
    with allure.step('Skip wellcome screen'):
        start_screen.skip_onboarding()
    with allure.step('Type search'):
        main_screen.click_search_form()
        main_screen.input_search_form('Appium')
    with allure.step('Verify content found'):
        results = search_screen.get_search_result()
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
    with allure.step('Open search result'):
        results.first.click()


def test_search_selenium(environment):
    with allure.step('Skip wellcome screen'):
        start_screen.skip_onboarding()
    with allure.step('Type search'):
        main_screen.click_search_form()
        main_screen.input_search_form('Selenium')
    with allure.step('Verify content found'):
        results = search_screen.get_search_result()
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selenium'))
    with allure.step('Open search result'):
        results.first.click()
