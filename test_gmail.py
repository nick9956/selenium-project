import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages.Base_page import WebDriverFactory, Chrome_alerts
from Pages.Sign_in_email_page import Sign_in_email_page as Sign_in_email
from Pages.Sign_in_password_page import Sign_in_password_page
from Pages.Inbox_page import Inbox_page, Compose_pop_up, Account_pop_up
from Pages.Email_page import Email_page
from Pages.Sign_out_page import Signout_page


class Test_Gmail(unittest.TestCase):
    email = 'mykola.rudym@nure.ua'
    password = "2203Rudim1712"
    subject_sender = 'Feeling'
    body_of_letter_sender = 'Hello! How are you?'

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverFactory.get_webdriver("chrome")

    def waiting(self, time):
        self.wait_element = WebDriverWait(self.driver, time)

    def compare_letter_text(self):
        email_page = Email_page(self.driver)
        self.assertEqual(self.body_of_letter_sender, email_page.get_letter_text())

    def compare_subject_text(self):
        email_page = Email_page(self.driver)
        self.assertEqual(self.subject_sender, email_page.get_subject_text())

    def compare_emails(self):
        email_page = Email_page(self.driver)
        self.assertEqual(Test_Gmail.email, email_page.get_sender_email())

    def test_step1_login_to_gmail(self):
        signin_email_page = Sign_in_email(self.driver)
        signin_email_page.get_start_page(Sign_in_email.url)
        signin_email_page.enter_and_submit_email(Test_Gmail.email)
        self.driver.implicitly_wait(5)
        signin_password_page = Sign_in_password_page(self.driver)
        signin_password_page.enter_and_submit_password(Test_Gmail.password)
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="gb_ne gb_qc gb_le"]')))

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
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="gb_ne gb_qc gb_le"]')))
        inbox_page = Inbox_page(self.driver)
        inbox_page.open_letter()
        self.waiting(5)
        self.wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="aju"]')))

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
        chrome_alerts = Chrome_alerts(self.driver)
        chrome_alerts.accept_alert()
        signout_page = Signout_page(self.driver)
        signout_page.verify_sign_out_message()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()











