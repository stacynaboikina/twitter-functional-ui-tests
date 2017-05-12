import json

from tools import config_paths_os


class DriverSetup(object):
    def __init__(self):
        with open(config_paths_os.DRIVER_CONFIG_PATH, "r") as driver_config:
            configs = json.loads(driver_config.read())
            self.address = configs["address"]
            self.browser = configs["browser"]
            if self.browser == "firefox":
                from selenium.webdriver import Firefox
                self.driver = Firefox()
            else:
                # todo: configure with other browsers
                raise NotImplemented()

    def __del__(self):
        self.driver.close()
