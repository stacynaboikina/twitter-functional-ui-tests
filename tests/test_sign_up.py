from tests.test_setup import test_base_setup
from tools.random_values import rand_name_generator


class TestSignUp(test_base_setup.TestBaseSetup):
    """
    Log in test scenarios for existing, non-existing users
    """
    def test_sign_up(self):
        """
        Description: Verify sign up with random values

        Pre-conditions:
            1. Open browser
            2. Connect to twitter.com
        Steps:
            1. Verify sign up form exists.
            2. Enter random username.
            3. Enter random email.
            4. Enter random password.
            5. Click Sign in button.
            6. Verify there is a redirect to join twitter page.
        """
        self.assertTrue(self.pages.home_page.sign_up_form,
                        "Sign up form should be present on the page")
        self.pages.home_page.sign_up_full_name_input_field.send_keys(
            rand_name_generator())
        self.pages.home_page.sign_up_email_input_field.send_keys(
            "{user}@{domain}.com".format(user=rand_name_generator(),
                                         domain=rand_name_generator()))
        self.pages.home_page.sign_up_password_input_field.click()
        self.pages.home_page.sign_up_password_input_field.send_keys(
            rand_name_generator())
        self.pages.home_page.sign_up_button.click()
        self.assertEqual(self.pages.join_twitter_page.join_twitter_header.text,
                         self.pages.join_twitter_page.page_title)
