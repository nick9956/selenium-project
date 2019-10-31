from framework.pages.base_page import PageObject
from selenium.webdriver.common.keys import Keys
from framework.config import Parser


class SignInPasswordPage(PageObject):

    # selectors
    PASSWORD_FIELD = '//*[@name="password"]'

    # class methods
    def enter_and_submit_password(self):
        password_field = self.driver.find_element_by_xpath(self.PASSWORD_FIELD)
        user_password = Parser()
        password_field.send_keys(user_password.read_valid_password())
        password_field.send_keys(Keys.ENTER)
