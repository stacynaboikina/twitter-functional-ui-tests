from unittest import TestCase

from pages_custom import twitter_pages
from tools import driver_setup
from tools import config_paths_os, config_obj


class TestBaseSetup(TestCase):

    def setUp(self, user_config=config_paths_os.EXISTING_USER_CONFIG_PATH):
        self.driver_setup = driver_setup.DriverSetup()
        self.pages = twitter_pages.TwitterPages(self.driver_setup.driver)
        self.user = config_obj.get_obj_from_config(user_config)
        self.driver_setup.driver.get(self.driver_setup.address)

    def tearDown(self):
        self.driver_setup.driver.close()

