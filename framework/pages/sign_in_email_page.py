from framework.pages.base_page import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from framework.pages.sign_in_password_page import SignInPasswordPage


class SignInEmailPage(PageObject):

    # selectors
    EMAIL_FIELD = '//*[@id="identifierId"]'

    # variables
    url = 'https://mail.google.com'

    # class methods
    def get_start_page(self):
        self.driver.get(SignInEmailPage.url)

    def enter_and_submit_email(self, email):
        email_field = self.driver.find_element_by_xpath(SignInEmailPage.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, SignInPasswordPage.PASSWORD_FIELD)))

