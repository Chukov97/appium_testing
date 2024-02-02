from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class MainScreen:
    SEARCH_FORM = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
    INPUT_FORM = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")

    def click_search_form(self):
        browser.element(self.SEARCH_FORM).click()
        return self

    def input_search_form(self, text):
        browser.element(self.INPUT_FORM).type(text).click()
        return self


main_screen = MainScreen()
