from selenium.common.exceptions import NoAlertPresentException

from framework.pages.base_page import PageObject


class ChromeAlerts(PageObject):

    def is_chrome_alert_present(self):
        try:
            self.driver.switch_to.alert()
            return True
        except NoAlertPresentException:
            print("Chrome Alert was not present")
            return False

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
