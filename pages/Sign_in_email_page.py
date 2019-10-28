from pages.Base_page import Page_Object, Users
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

    def enter_and_submit_email(self):
        email_field = self.driver.find_element_by_xpath(Sign_in_email_page.EMAIL_FIELD)
        email_field.clear()
        user = Users()
        email_field.send_keys(user.get_email('Mykola'))
        email_field.send_keys(Keys.ENTER)

