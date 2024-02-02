from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SearchScreen:
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
    OPEN_SEARCH_RESULT = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")

    # OPEN_SEARCH_RESULT = (AppiumBy.CLASS_NAME, "android.view.ViewGroup")
    # OPEN_SEARCH_RESULT = (AppiumBy.XPATH,
    #                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]")

    def get_search_result(self):
        return browser.all(self.SEARCH_RESULT)

    def open_search_result(self):
        browser.all(self.OPEN_SEARCH_RESULT)[0].click()
        return self


search_screen = SearchScreen()
