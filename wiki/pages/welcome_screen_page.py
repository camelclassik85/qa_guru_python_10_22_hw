from selene import browser, have
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy


class WelcomeScreenPage:

    def __init__(self):
        self.primaryTextView = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        self.button_continue = browser.element((AppiumBy.ID,
                                                'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
        self.button_get_started = browser.element((AppiumBy.ID,
                                                   'org.wikipedia.alpha:id/fragment_onboarding_done_button'))
        self.skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))

    def check_welcome_screen(self):
        with step('First welcome screen and click to Continue'):
            self.primaryTextView.should(have.text('The Free Encyclopedia\n…in over 300 languages'))
            self.button_continue.click()
        with step(f'Checking second page and click to Continue'):
            self.primaryTextView.should(have.text('New ways to explore'))
            self.button_continue.click()
        with step(f'Checking third page and click to Continue'):
            self.primaryTextView.should(have.text('Reading lists with sync'))
            self.button_continue.click()
        with step(f'Checking fourth page and click to Geet started'):
            self.primaryTextView.should(have.text('Data & Privacy'))
            self.button_get_started.click()

    def skip_welcome_screen(self):
        self.skip_button.click()


welcome_screen = WelcomeScreenPage()