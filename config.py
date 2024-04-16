import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from utils.resource import path
from pydantic_settings import BaseSettings

load_dotenv('.env.credentials')

class Config(BaseSettings):
    timeout: float = float(os.getenv('TIMEOUT'))
    remote_url: str = os.getenv('REMOTE_URL')
    platform_version: str = os.getenv('PLATFORM_VERSION', '')
    device_name: str = os.getenv('DEVICE_NAME', '')
    app_wait_activity: str = os.getenv("appWaitActivity", '')
    app: str = os.getenv('APP')
    # load_dotenv('.env.credentials')
    user_name: str = os.getenv('USER_NAME')
    access_key: str = os.getenv('ACCESS_KEY')

    def to_driver_options(self, context):
        options = UiAutomator2Options()
        if context == 'emulator_local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', path(self.app))

        if context == 'real_local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', path(self.app))

        if context == 'bstack':
            options.set_capability('remote_url', self.URL)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options',
                {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": self.user_name,
                    "accessKey": self.access_key,
                },
            )
        return options


run_config = Config()
