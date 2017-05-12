from pages_custom import page_ids


class HomePage(object):
    def __init__(self, driver):
        self.__driver = driver

    @property
    def login_input_field(self):
        return self.__driver.find_element_by_id(
            page_ids.LogInPage.log_in_field)

    @property
    def password_input_field(self):
        return self.__driver.find_element_by_id(
            page_ids.LogInPage.password_field)

    @property
    def log_in_button(self):
        element = self.__driver.find_element_by_css_selector(
            "button[class='submit btn primary-btn flex-table-btn js-submit']")
        return element

    @property
    def sign_up_form(self):
        return self.__driver.find_element_by_id("frontpage-signup-form")

    @property
    def sign_up_full_name_input_field(self):
        return self.sign_up_form.find_element_by_xpath(
            "//input[@placeholder='Full name']")

    @property
    def sign_up_email_input_field(self):
        return self.sign_up_form.find_element_by_xpath(
            "//input[@placeholder='Email']")

    @property
    def sign_up_password_input_field(self):
        return self.sign_up_form.find_element_by_xpath(
            "//input[@name='user[user_password]']")

    @property
    def sign_up_button(self):
        return self.__driver.find_element_by_css_selector(
            "button[class='btn signup-btn u-floatRight']")

    @property
    def current_language_button(self):
        return self.__driver.find_element_by_class_name("js-current-language")

    @property
    def available_languages_dropdown(self):
        return self.__driver.find_element_by_class_name("js-language-dropdown")

    @property
    def available_languages(self):
        return self.available_languages_dropdown.find_elements_by_tag_name("a")

    def get_lanugage_by_text_name(self, language):
        for element in self.available_languages:
            if element.text == language:
                return element

    def log_in(self, username, password):
        self.login_input_field.send_keys(username)
        self.password_input_field.send_keys(password)
        self.log_in_button.click()

