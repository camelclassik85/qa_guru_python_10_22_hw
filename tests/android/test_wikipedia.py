import allure
from wiki.constants import Constants
from wiki.pages.main_page import main_page
from wiki.pages.welcome_screen_page import welcome_screen


def test_welcome_screen_shows():
    with allure.step('Check welcome screen'):
        welcome_screen.check_welcome_screen()
    with allure.step('CheckmMain Page elements shows'):
        main_page.check_main_page_elements_shows()


def test_search():
    with allure.step('Skip welcome screen'):
        welcome_screen.skip_welcome_screen()

    with allure.step('Type search Appium'):
        main_page.search_text(Constants.text_appium)

    with allure.step('Verify content found'):
        main_page.verify_search_and_quantity_results(Constants.text_appium)


def test_another_search():
    with allure.step('Skip welcome screen'):
        welcome_screen.skip_welcome_screen()

    with allure.step('Type search Android'):
        main_page.search_text(Constants.text_android)

    with allure.step('Open content page'):
        main_page.verify_search_and_quantity_results(Constants.text_android)
