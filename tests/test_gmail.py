import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from framework.pages.sign_in_email_page import SignInEmailPage
from framework.pages.inbox_page import *
from framework.pages.email_page import EmailPage
from framework.application import Application


class TestGmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Application()
        cls.config = Config()

    def waiting(self, time):
        self.wait_element = WebDriverWait(self. app.driver, time)

    def compare_letter_text(self):
        self.assertEqual(AccountPopUp.body_of_letter_sender, self.app.email_page.get_letter_text())

    def compare_subject_text(self):
        self.assertEqual(AccountPopUp.subject_sender, self.app.email_page.get_subject_text())

    def compare_emails(self):
        self.assertEqual(self.config.valid_email, self.app.email_page.get_sender_email())

    def test_step1_login_to_gmail(self):
        self.app.signin_email_page.get_start_page(SignInEmailPage.url)
        self.app.signin_email_page.enter_and_submit_email(self.config.valid_email)
        self.app.driver.implicitly_wait(5)
        self.app.signin_password_page.enter_and_submit_password(self.config.valid_password)
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, InboxPage.GMAIL_LOGO)))

    def test_step2_letter_to_myself(self):
        self.app.compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.app.driver.find_element_by_xpath(ComposePopUp.COMPOSE_POP_UP).is_displayed()
        self.app.compose_pop_up.fill_to_field(self.config.valid_email)
        self.app.compose_pop_up.fill_subject_field(ComposePopUp.subject_sender)
        self.app.compose_pop_up.fill_body_of_letter(ComposePopUp.body_of_letter_sender)
        self.app.compose_pop_up.click_send_button()

    def test_step3_open_letter(self):
        self.app.compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, InboxPage.GMAIL_LOGO)))
        self.app.inbox_page.open_letter()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, EmailPage.LOGO_OF_SENDER)))

    def test_step4_match_text_in_letter(self):
        self.compare_emails()
        self.compare_subject_text()
        self.compare_letter_text()

    def test_step5_logout(self):
        self.app.account_pop_up.open_account_information_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, self.app.account_pop_up.ACCOUNT_POP_UP)))
        self.app.account_pop_up.click_sign_out_button()
        self.waiting(2)
        self.app.chrome_alerts.is_chrome_alert_present()
        self.app.chrome_alerts.accept_alert()
        self.app.signout_page.verify_sign_out_message()

    @classmethod
    def tearDownClass(cls):
        cls.initialization_class.driver.quit()











