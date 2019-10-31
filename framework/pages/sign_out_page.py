from framework.pages.base_page import PageObject
import unittest


class Signout_page(PageObject):

    #selectors
    SIGNED_OUT_LABEL = '//*[@class="cRiDhf"]'

    #class methods
    def get_sign_out_text_message(self):
        sign_out_message = self.driver.find_element_by_xpath(self.SIGNED_OUT_LABEL).text
        return sign_out_message

    def verify_sign_out_message(self):
        test_case = unittest.TestCase()
        test_case.assertEqual('Ви вийшли з облікового запису', self.get_sign_out_text_message())
