from pages_custom import home_page
from pages_custom import login_error_page
from pages_custom import error_messages
from pages_custom import join_twitter_page


class TwitterPages(object):
    def __init__(self, driver):
        self.home_page = home_page.HomePage(driver)
        self.login_error_page = login_error_page.LogInErrorPage(driver)
        self.join_twitter_page = join_twitter_page.JoinTwitterPage(driver)

        self.error_messages = error_messages.ErrorMessages
