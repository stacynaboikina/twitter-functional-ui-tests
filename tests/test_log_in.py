from parameterized import parameterized

from tests.test_setup import test_base_setup
from tools.random_values import rand_name_generator


class TestLogIn(test_base_setup.TestBaseSetup):
    """
    Log in test scenarios for existing, non-existing users
    """
    def test_log_in_as_existing_user_by_username(self):
        """
        Description: Verify usernmae-based log in as existing twitter user

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps:
            1. Check there is no "auth_token" cookie before user login.
            2. Input existsing username and password.
            3. Check "auth_token" cookie was created and has some data.
        """
        self.assertFalse(self.driver_setup.driver.get_cookie("auth_token"),
                         "User auth_token cookie should be created after "
                         " login only")
        self.pages.home_page.log_in(self.user.username, self.user.password)
        self.assertTrue(self.driver_setup.driver.get_cookie("auth_token"),
                        "User should get a cookie with auth_token after "
                        "login")

    def test_log_in_as_existing_user_by_email(self):
        """
        Description: Verify email-based log in as existing twitter user

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps:
            1. Check there is no "auth_token" cookie before user login.
            2. Input existsing user email and password.
            3. Check "auth_token" cookie was created and has some data.
        """
        self.assertFalse(self.driver_setup.driver.get_cookie("auth_token"),
                         "User auth_token cookie should be created after "
                         " login only")
        self.pages.home_page.log_in(self.user.email, self.user.password)
        self.assertTrue(self.driver_setup.driver.get_cookie("auth_token"),
                        "User should get a cookie with auth_token after "
                        "login")

    @parameterized.expand([
        ("random_names", rand_name_generator(), rand_name_generator()),
        ("empty_strings", "", ""),
        ("spaces", " ", " ")])
    def test_log_in_as_non_existing_user(self, name, username, password):
        """
        Description: Verify non-existing user log in given the above values.

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps for each value above:
            1. Input incorrect username and incorrect password.
            2. Check no "auth_token" cookie was created.
            3. Verify there is an alert message.

        Steps:
        :param name: test method name
        :param username: non-existing username
        :param password: non-existing password
        """
        self.pages.home_page.log_in(username, password)
        self.assertFalse(self.driver_setup.driver.get_cookie("auth_token"),
                         "User 'auth_token cookie should not be created, "
                         "as username/password are incorrect'")
        self.assertTrue(self.pages.login_error_page.alert_message)
        self.assertEqual(
            str(self.pages.login_error_page.user_does_not_exist_message.text),
            self.pages.error_messages.user_does_not_exist)
