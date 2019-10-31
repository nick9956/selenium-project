from framework.pages.base_page import PageObject
from selenium.webdriver.common.keys import Keys
from framework.config import Parser


class SignInEmailPage(PageObject):

    # selectors
    EMAIL_FIELD = '//*[@id="identifierId"]'

    # variables
    url = 'https://mail.google.com'

    # class methods
    def get_start_page(self, url):
        self.url = url
        self.driver.get(url)

    def enter_and_submit_email(self):
        email_field = self.driver.find_element_by_xpath(SignInEmailPage.EMAIL_FIELD)
        email_field.clear()
        email = Parser()
        email_field.send_keys(email.read_valid_email())
        email_field.send_keys(Keys.ENTER)

