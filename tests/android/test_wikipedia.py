import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from wiki.pages.main_page import main_page
from wiki.pages.welcome_screen_page import welcome_screen


def test_welcome_screen_shows():
    welcome_screen.check_welcome_screen()
    main_page.check_main_page_elements_shows()


# def test_search():
#     with allure.step('Skip welcome screen'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
#
#     with allure.step('Type search Appium'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
#         browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")
#
#     with allure.step('Verify content found'):
#         results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
#         results.should(have.size_greater_than(0))
#         results.first.should(have.text("Appium"))


# def test_another_search():
#     with allure.step('Skip welcome screen'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
#
#     with allure.step('Type search Android'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
#         browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Android")
#
#     with allure.step('Open content page'):
#         results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
#         results.should(have.size_greater_than(0))
#         results.first.should(have.text("Android")).click()
