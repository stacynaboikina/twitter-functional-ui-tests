class JoinTwitterPage(object):
    def __init__(self, driver):
        self.__driver = driver
        self.page_title = "Join Twitter today."

    @property
    def join_twitter_header(self):
        return self.__driver.find_element_by_tag_name("h1")
