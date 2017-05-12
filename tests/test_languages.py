import json
import os
from parameterized import parameterized

from tests.test_setup import test_base_setup
from tools.config_paths_os import CONFIGS_PATH


class TestLanguages(test_base_setup.TestBaseSetup):
    def test_languages_list(self):
        """
        Description: Verify all supported languages are displayed on home
        page.

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps:
            1. Click Current Language button.
            2. Verify there are languages to select in the drop-down.
            3. Verify for each expected language actually exists on the page.
        """
        self.pages.home_page.current_language_button.click()
        self.assertTrue(len(self.pages.home_page.available_languages) > 0,
                        "There should be multiple languages to select")
        with open(os.path.join(CONFIGS_PATH, "available_languages.json"),
                  "r") as lang_configs:
            available_languages = json.loads(
                lang_configs.read())["available_languages"]
            for language in self.pages.home_page.available_languages:
                self.assertTrue(language.text in available_languages,
                                "Could not find language".format(str(
                                    language.text.encode('utf-8').strip())))

    @parameterized.expand([
        ("swedish", "Svenska", "Logga in")])
    def test_lanugage_switch(self, name, language, log_in_button_text):
        """
        Description: Verify changing the language to given one.

        :param name: test method name
        :param language: str, available language to select from drop-down
        :param log_in_button_text: log in button text in chosen language

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps:
            1. Click Current Language button.
            2. Pick given language from available ones in the drop-down.
            3. Check log in button text changed to expected (given) one.
        """
        self.pages.home_page.current_language_button.click()
        self.pages.home_page.get_lanugage_by_text_name(language).click()
        self.assertEqual(self.pages.home_page.log_in_button.text,
                         log_in_button_text,
                         "Log in button should have polish text")
