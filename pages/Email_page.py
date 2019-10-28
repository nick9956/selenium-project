from pages.Base_page import Page_Object, Users
import unittest


class Email_page(Page_Object):

    #selectors
    RECEIVED_MESSAGE_BODY = '//*[@class="a3s aXjCH "]/div[1]'
    RECEIVED_SUBJECT = '//*[@class="hP"]'
    NAME_OF_SENDER = '//*[@class="gD"]'
    LOGO_OF_SENDER = '//*[@class="aju"]'

    #class methods
    def get_letter_text(self):
        body_of_letter_recipient = self.driver.find_element_by_xpath(self.RECEIVED_MESSAGE_BODY).text
        return body_of_letter_recipient

    def get_subject_text(self):
        subject_recipient = self.driver.find_element_by_xpath(self.RECEIVED_SUBJECT).text
        return subject_recipient

    def get_sender_email(self):
        username_in_recipient = self.driver.find_element_by_xpath(self.NAME_OF_SENDER).get_attribute('email')
        return username_in_recipient

    def compare_emails(self):
        test_case = unittest.TestCase()
        user_email = Users()
        test_case.assertEqual(user_email.get_email('Mykola'), self.get_sender_email())
