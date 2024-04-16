import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from appium import webdriver
from config import run_config
from utils import allure_attach
from utils.resource import path


@allure.step('Select platform according running test folder')
def pytest_addoption(parser):
    parser.addoption("--context", action="store", default="emulator_local")


def pytest_configure(config):
    context = config.getoption('--context')
    dotenv_path = path(f'.env.{context}')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    with allure.step('Driver config create'):
        options = run_config.to_driver_options(context=context)

        browser.config.driver = webdriver.Remote(run_config.remote_url, options=options)
        browser.config.timeout = run_config.timeout

    yield

    session_id = browser.driver.session_id

    with allure.step('Add screenshot'):
        allure_attach.attach_screenshot(browser)

    with allure.step('Add html'):
        allure_attach.attach_xml(browser)

    with allure.step('tear down app session id: ' + session_id):
        browser.quit()

    if context == 'bstack':
        with allure.step('Add video'):
            allure_attach.attach_video(session_id)
