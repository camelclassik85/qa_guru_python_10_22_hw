from selene import browser, be, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    def __init__(self):
        self.wiki_logo = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark'))
        self.search_field = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container'))
        self.search_input_first = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        self.search_input_second = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        self.search_results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))

    def check_main_page_elements_shows(self):
        with allure.step('Check search filed is presence'):
            self.search_field.should(be.clickable)
            self.search_field.should(be.visible)

    def search_text(self, text):
        self.search_input_first.click()
        self.search_input_second.type(text)

    def verify_search_and_quantity_results(self, text):
        self.search_results.should(have.size_greater_than(0))
        self.search_results.first.should(have.text(text))


main_page = MainPage()
