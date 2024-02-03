from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query


class MainScreen:
    TEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Text Button")
    TEXT_INPUT = (AppiumBy.ACCESSIBILITY_ID, "Text Input")
    TEXT_OUTPUT = (AppiumBy.ACCESSIBILITY_ID, "Text Output")

    def click_text_button(self):
        browser.element(self.TEXT_BUTTON).click()
        return self

    def input_text(self, text):
        browser.element(self.TEXT_INPUT).type(text)
        return self

    def get_output_text(self):
        return browser.element(self.TEXT_OUTPUT).get(query.text)


main_screen = MainScreen()
