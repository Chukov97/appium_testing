from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SearchScreen:
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
    OPEN_SEARCH_RESULT = (AppiumBy.CLASS_NAME, "android.view.ViewGroup")

    def get_search_result(self):
        return browser.all(self.SEARCH_RESULT)

    def open_search_result(self):
        browser.element(self.OPEN_SEARCH_RESULT).click()
        return self


search_screen = SearchScreen()
