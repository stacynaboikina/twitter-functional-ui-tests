class LogInErrorPage(object):
    def __init__(self, driver):
        self.__driver = driver

    @property
    def alert_message(self):
        return self.__driver.find_element_by_class_name("alert-messages")

    @property
    def user_does_not_exist_message(self):
        return self.__driver.find_element_by_class_name("message-text")
