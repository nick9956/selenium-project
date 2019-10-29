import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.Base_page import WebDriverFactory, Chrome_alerts, Users
from pages.Sign_in_email_page import Sign_in_email_page as Sign_in_email
from pages.Sign_in_password_page import Sign_in_password_page
from pages.Inbox_page import Inbox_page, Compose_pop_up, Account_pop_up
from pages.Email_page import Email_page
from pages.Sign_out_page import Signout_page


class Test_Gmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverFactory.get_webdriver("chrome")

    def waiting(self, time):
        self.wait_element = WebDriverWait(self.driver, time)

    def compare_letter_text(self):
        email_page = Email_page(self.driver)
        self.assertEqual(Account_pop_up.body_of_letter_sender, email_page.get_letter_text())

    def compare_subject_text(self):
        email_page = Email_page(self.driver)
        self.assertEqual(Account_pop_up.subject_sender, email_page.get_subject_text())

    def compare_emails(self):
        email_page = Email_page(self.driver)
        user = Users()
        self.assertEqual(user.get_email('Mykola'), email_page.get_sender_email())

    def test_step1_login_to_gmail(self):
        signin_email_page = Sign_in_email(self.driver)
        signin_email_page.get_start_page(Sign_in_email.url)
        signin_email_page.enter_and_submit_email()
        self.driver.implicitly_wait(5)
        signin_password_page = Sign_in_password_page(self.driver)
        signin_password_page.enter_and_submit_password()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, Inbox_page.GMAIL_LOGO)))

    def test_step2_letter_to_myself(self):
        compose_pop_up = Compose_pop_up(self.driver)
        compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.driver.find_element_by_xpath(Compose_pop_up.COMPOSE_POP_UP).is_displayed()
        compose_pop_up.fill_to_field()
        compose_pop_up.fill_subject_field()
        compose_pop_up.fill_body_of_letter()
        compose_pop_up.click_send_button()

    def test_step3_open_letter(self):
        compose_pop_up = Compose_pop_up(self.driver)
        compose_pop_up.open_compose_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, Inbox_page.GMAIL_LOGO)))
        inbox_page = Inbox_page(self.driver)
        inbox_page.open_letter()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, Email_page.LOGO_OF_SENDER)))

    def test_step4_match_text_in_letter(self):
        self.compare_emails()
        self.compare_subject_text()
        self.compare_letter_text()

    def test_step5_logout(self):
        account_pop_up = Account_pop_up(self.driver)
        account_pop_up.open_account_information_pop_up()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, account_pop_up.ACCOUNT_POP_UP)))
        account_pop_up.click_sign_out_button()
        self.waiting(5)
        chrome_alerts = Chrome_alerts(self.driver)
        if(self.wait_element.until(ec.alert_is_present())==None):
            print("Chrome Alert was not present")
        else:
            chrome_alerts.accept_alert()
        signout_page = Signout_page(self.driver)
        signout_page.verify_sign_out_message()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()











