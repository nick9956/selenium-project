from pages.Base_page import Page_Object, Users
from selenium.webdriver.common.keys import Keys


class Sign_in_password_page(Page_Object):

    # selectors
    PASSWORD_FIELD = '//*[@name="password"]'

    #variables
    password = "2203Rudim1712"

    # class methods
    def enter_and_submit_password(self):
        password_field = self.driver.find_element_by_xpath(self.PASSWORD_FIELD)
        user_password = Users()
        password_field.send_keys(user_password.get_password('Mykola'))
        password_field.send_keys(Keys.ENTER)
