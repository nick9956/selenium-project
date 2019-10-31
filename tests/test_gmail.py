import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from framework.web_driver_factory import WebDriverFactory
from framework.chrome_alerts import ChromeAlerts
from framework.pages.sign_in_email_page import SignInEmailPage as Sign_in_email
from framework.pages.sign_in_password_page import SignInPasswordPage
from framework.pages.inbox_page import InboxPage, ComposePopUp, AccountPopUp
from framework.pages.email_page import EmailPage
from framework.pages.sign_out_page import Signout_page
from framework.config import Parser


class TestGmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverFactory.get_webdriver("chrome")

    def waiting(self, time):
        self.wait_element = WebDriverWait(self.driver, time)

    def compare_letter_text(self):
        email_page = EmailPage(self.driver)
        self.assertEqual(AccountPopUp.body_of_letter_sender, email_page.get_letter_text())

    def compare_subject_text(self):
        email_page = EmailPage(self.driver)
        self.assertEqual(AccountPopUp.subject_sender, email_page.get_subject_text())

    def compare_emails(self):
        email_page = EmailPage(self.driver)
        user_email = Parser()
        self.assertEqual(user_email.read_valid_email(), email_page.get_sender_email())

    def test_step1_login_to_gmail(self):
        signin_email_page = Sign_in_email(self.driver)
        signin_email_page.get_start_page(Sign_in_email.url)
        signin_email_page.enter_and_submit_email()
        self.driver.implicitly_wait(5)
        signin_password_page = SignInPasswordPage(self.driver)
        signin_password_page.enter_and_submit_password()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, InboxPage.GMAIL_LOGO)))

    def test_step2_letter_to_myself(self):
        compose_pop_up = ComposePopUp(self.driver)
        compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.driver.find_element_by_xpath(ComposePopUp.COMPOSE_POP_UP).is_displayed()
        compose_pop_up.fill_to_field()
        compose_pop_up.fill_subject_field()
        compose_pop_up.fill_body_of_letter()
        compose_pop_up.click_send_button()

    def test_step3_open_letter(self):
        compose_pop_up = ComposePopUp(self.driver)
        compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, InboxPage.GMAIL_LOGO)))
        inbox_page = InboxPage(self.driver)
        inbox_page.open_letter()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, EmailPage.LOGO_OF_SENDER)))

    def test_step4_match_text_in_letter(self):
        self.compare_emails()
        self.compare_subject_text()
        self.compare_letter_text()

    def test_step5_logout(self):
        account_pop_up = AccountPopUp(self.driver)
        account_pop_up.open_account_information_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, account_pop_up.ACCOUNT_POP_UP)))
        account_pop_up.click_sign_out_button()
        self.waiting(2)
        chrome_alerts = ChromeAlerts(self.driver)
        chrome_alerts.is_chrome_alert_present()
        chrome_alerts.accept_alert()
        signout_page = Signout_page(self.driver)
        signout_page.verify_sign_out_message()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()











