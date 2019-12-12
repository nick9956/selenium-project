from framework.pages.inbox_page import ComposePopUp
from framework.application import Application
from framework.pages.email_page import EmailPage
from framework.pages.sign_out_page import Signout_page
import random


class TestGmail(object):

    app = None

    @classmethod
    def setup_class(cls):
        cls.app = Application()
        rnd_numbers = str(random.randint(1, 10000000))
        cls.rnd_subject = ComposePopUp.subject_sender + rnd_numbers + '_automation'
        cls.rnd_body = ComposePopUp.body_of_letter_sender + rnd_numbers + '_automation'

    def verify_sign_in_email_page(self):
        expected_title = 'Gmail'
        assert(expected_title == self.app.driver.title)

    def verify_sign_in_password_page(self):
        expected_title = 'Gmail'
        assert(expected_title == self.app.driver.title)

    def verify_inbox_page(self):
        expected_url = 'https://mail.google.com/mail/u/0/#inbox'
        assert(expected_url == self.app.driver.current_url)

    def verify_email_page(self):
        list_of_attributes = [EmailPage.LOGO_OF_SENDER, EmailPage.NAME_OF_SENDER, EmailPage.RECEIVED_SUBJECT, EmailPage.RECEIVED_MESSAGE_BODY]
        for element in list_of_attributes:
            self.app.driver.find_element_by_xpath(element)

    def verify_sign_out_email_page(self):
        expected_title = 'Gmail'
        assert (expected_title == self.app.driver.title)
        self.app.driver.find_element_by_xpath(Signout_page.SIGNED_OUT_LABEL)

    def compare_letter_text(self):
        assert(self.rnd_body == self.app.email_page.get_letter_text())

    def compare_subject_text(self):
        assert(self.rnd_subject == self.app.email_page.get_subject_text())

    def compare_emails(self):
        assert (self.app.config.valid_email == self.app.email_page.get_sender_email())

    def verify_sign_out_message(self):
        assert ('Ви вийшли з облікового запису' == self.app.signout_page.get_sign_out_text_message())

    def test_login_to_gmail(self):
        self.app.signin_email_page.get_start_page()
        self.verify_sign_in_email_page()
        self.app.signin_email_page.enter_and_submit_email(self.app.config.valid_email)
        self.verify_sign_in_password_page()
        self.app.signin_password_page.enter_and_submit_password(self.app.config.valid_password)
        self.verify_inbox_page()

    def test_letter_to_myself(self):
        self.app.compose_pop_up.open_compose_pop_up()
        self.app.compose_pop_up.fill_to_field(self.app.config.valid_email)
        self.app.compose_pop_up.fill_subject_field(self.rnd_subject)
        self.app.compose_pop_up.fill_body_of_letter(self.rnd_body)
        self.app.compose_pop_up.click_send_button()

    def test_open_letter(self):
        self.app.driver.implicitly_wait(1)
        self.app.inbox_page.open_letter(self.rnd_subject)
        self.verify_email_page()

    def test_match_text_in_letter(self):
        self.compare_emails()
        self.compare_subject_text()
        self.compare_letter_text()

    def test_delete_letter(self):
        self.app.inbox_page.open_inbox_page()
        self.verify_inbox_page()
        self.app.inbox_page.delete_last_letter()

    def test_logout(self):
        self.app.account_pop_up.open_account_information_pop_up()
        self.app.account_pop_up.click_sign_out_button()
        self.app.driver.implicitly_wait(1)
        self.app.chrome_alerts.is_chrome_alert_present_accept_it()
        self.verify_sign_out_email_page()
        self.verify_sign_out_message()

    @classmethod
    def teardown_class(cls):
        cls.app.driver.quit()











