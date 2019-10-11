from Pages.Base_page import Page_Object
from selenium.webdriver.common.keys import Keys


class Sign_in_email_page(Page_Object):

    # selectors
    EMAIL_FIELD = '//*[@id="identifierId"]'

    #variables
    url = 'https://mail.google.com'

    # class methods
    def get_start_page(self, url):
        self.url = url
        self.driver.get(url)

    def enter_and_submit_email(self, email):
        email_field = self.driver.find_element_by_xpath(Sign_in_email_page.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)

