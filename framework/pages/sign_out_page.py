from framework.pages.base_page import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Signout_page(PageObject):

    #selectors
    SIGNED_OUT_LABEL = '//*[@class="cRiDhf"]'

    #class methods
    def get_sign_out_text_message(self):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, Signout_page.SIGNED_OUT_LABEL)))
        return self.driver.find_element_by_xpath(self.SIGNED_OUT_LABEL).text
