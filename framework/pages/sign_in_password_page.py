from framework.pages.base_page import PageObject
from selenium.webdriver.common.keys import Keys


class SignInPasswordPage(PageObject):

    # selectors
    PASSWORD_FIELD = '//*[@name="password"]'

    # class methods
    def enter_and_submit_password(self, password):
        password_field = self.driver.find_element_by_xpath(self.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
