from selenium.common.exceptions import NoAlertPresentException
from framework.pages.base_page import PageObject


class ChromeAlerts(PageObject):

    def is_chrome_alert_present_accept_it(self):
        try:
            self.driver.switch_to.alert.accept()
            return True
        except NoAlertPresentException:
            print("Chrome Alert was not present")
            return False
