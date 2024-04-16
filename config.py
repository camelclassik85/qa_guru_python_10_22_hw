import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from utils.resource import path
from pydantic import BaseModel
'''
from pydantic_settings import BaseSettings
 но тогда нужно будет дефолтное значение у переменных указать platform_version, platform_name, device_name, 
 app_wait_activity
'''


class Config(BaseModel):
    timeout: float = float(os.getenv('TIMEOUT'))
    remote_url: str = os.getenv('REMOTE_URL')
    platform_version: str = os.getenv('PLATFORM_VERSION')
    platform_name: str = os.getenv("PLATFORM_NAME")
    device_name: str = os.getenv('DEVICE_NAME')
    app_wait_activity: str = os.getenv("appWaitActivity")
    app: str = os.getenv('APP')
    bstack: bool = os.getenv('BSTACK', False)
    if bstack:
        load_dotenv('.env.credentials')
        user_name: str = os.getenv('USER_NAME')
        access_key: str = os.getenv('ACCESS_KEY')
    else:
        user_name: str = ''
        access_key: str = ''

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
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    "projectName": "Android app Python project",
                    "buildName": "android-browserstack-build",
                    "sessionName": "Android",
                    "userName": self.user_name,
                    "accessKey": self.access_key,
                },
            )
        return options


run_config = Config()
