import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from utils.file import abs_path_from_project
import pydantic


class Config(pydantic.BaseModel):
    load_dotenv()
    user_name: str = os.getenv('USER_NAME')
    access_key: str = os.getenv('ACCESS_KEY')

    app: str = os.getenv('APP')
    remote_url: str = os.getenv('REMOTE_URL')
    udid: str = os.getenv('UDID')
    device_name: str = os.getenv('DEVICE_NAME')
    app_wait_activity: str = os.getenv('APP_WAIT_ACTIVITY')
    timeout: float = 10.0

    build_name: str = os.getenv('BUILD_NAME')
    project_name: str = os.getenv('PROJECT_NAME')
    session_name: str = os.getenv('SESSION_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION')

    def driver_options(self, environment):
        options = UiAutomator2Options()

        if environment == 'local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('app', abs_path_from_project(self.app))
            options.set_capability('udid', self.udid)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('appWaitActivity', self.app_wait_activity)

        elif environment == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('app', self.app)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability(
                'bstack:options', {
                    'projectName': self.project_name,
                    'buildName': self.build_name,
                    'sessionName': self.sessionName,
                    'userName': self.user_name,
                    'accessKey': self.access_key,
                },
            )

        return options


config = Config()
