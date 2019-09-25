import unittest
import mypkg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Test_Gmail(unittest.TestCase):
    username_sender = 'mikola.rudim@gmail.com'
    subject_sender = 'Feeling'
    body_of_letter_sender = 'Hello! How are you?'

    @classmethod
    def setUpClass(cls):
        cls.driver = mypkg.getOrCreateWebdriver()

    def test_step1_login_to_gmai(self):
        self.driver.get('https://mail.google.com')
        email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.clear()
        email.send_keys(self.username_sender)
        email.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(5)
        password = self.driver.find_element_by_name('password')
        password.send_keys("2203Rudim1712")
        password.send_keys(Keys.ENTER)
        global wait_element
        wait_element = WebDriverWait(self.driver, 5)
        wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="gb_ne gb_qc gb_le"]')))

    def test_step2_letter_to_myself(self):
        self.driver.find_element_by_xpath('//*[@class="T-I J-J5-Ji T-I-KE L3"]').click()
        self.driver.find_element_by_xpath('//*[@class="AD"]').is_displayed()
        self.driver.find_element_by_xpath('//*[@name="to"]').send_keys(self.username_sender)
        self.driver.find_element_by_xpath('//*[@name="subjectbox"]').send_keys(self.subject_sender)
        self.driver.find_element_by_xpath('//*[@class="Am Al editable LW-avf tS-tW"]').send_keys(self.body_of_letter_sender)
        send_button = self.driver.find_element_by_xpath('//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
        send_button.click()

    def test_step3_open_letter(self):
        self.driver.find_element_by_xpath('//*[@class="nU n1"]').click()
        wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="gb_ne gb_qc gb_le"]')))
        letter = self.driver.find_element_by_xpath('//*[@class="bog"]/span[contains(.,"Feeling")]')
        letter.click()
        wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="aju"]')))

    def test_step4_match_text_in_letter(self):
        body_of_letter_recipient = self.driver.find_element_by_xpath('//*[@class="a3s aXjCH "]/div[1]').text
        self.assertEqual(self.body_of_letter_sender, body_of_letter_recipient)
        subject_recipient = self.driver.find_element_by_xpath('//*[@class="hP"]').text
        self.assertEqual(self.subject_sender, subject_recipient)
        username_in_recipient = self.driver.find_element_by_xpath('//*[@class="gD"]').get_attribute('email')
        self.assertEqual(self.username_sender, username_in_recipient)

    def test_step5_logout(self):
        self.driver.find_element_by_xpath('//*[@class="gb_B gb_Da gb_g"]').click()
        wait_element.until(ec.presence_of_element_located((By.XPATH, '//*[@class="gb_Sa gb_D gb_Ec"]')))
        self.driver.find_element_by_xpath('//*[@class="gb_0 gb_9f gb_hg gb_Se gb_pb"]').click()
        self.driver.switch_to.alert.accept()
        logout_message = self.driver.find_element_by_xpath('//*[@class="cRiDhf"]').text
        self.assertEqual('Ви вийшли з облікового запису', logout_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()











