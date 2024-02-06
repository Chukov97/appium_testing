from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class StartScreen:
    SKIP_BUTTON = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')

    def skip_onboarding(self):
        return browser.element(self.SKIP_BUTTON).click()


start_screen = StartScreen()
