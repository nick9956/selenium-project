from framework.pages.base_page import PageObject
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from framework.pages.inbox_page import InboxPage


class SignInPasswordPage(PageObject):

    # selectors
    PASSWORD_FIELD = '//*[@name="password"]'

    # class methods
    def enter_and_submit_password(self, password):
        password_field = self.driver.find_element_by_xpath(self.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, InboxPage.GMAIL_LOGO)))
