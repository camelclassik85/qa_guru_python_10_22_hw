from selene import browser, be
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    def __init__(self):
        self.wiki_logo = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark'))
        self.search_field = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container'))

    def check_main_page_elements_shows(self):
        with step('Check search filed is presence'):
            self.search_field.should(be.clickable)
            self.search_field.should(be.visible)


main_page = MainPage()
