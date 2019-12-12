from framework.pages.base_page import PageObject
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from framework.pages.email_page import EmailPage


class InboxPage(PageObject):

    # selectors
    COMPOSE_BUTTON = '//*[@class="T-I J-J5-Ji T-I-KE L3"]'
    NAV_MENU = '//*[@class="nH oy8Mbf nn aeN bhZ"]'
    HIDDEN_INBOX_BUTTON = '//*[@class="J-Ke n0" and @tabindex="0"]'
    GMAIL_LOGO = '//*[@class="gb_la"]'
    LAST_LETTER_CHECKBOX = '//*[@class="Cp"]/div/table/tbody/tr[1]'
    DELETE_BUTTON = '//*[@class="ar9 T-I-J3 J-J5-Ji"]'

    # class methods
    def open_inbox_page(self):
        nav_menu = self.driver.find_element_by_xpath(self.NAV_MENU)
        hidden_inbox_button = self.driver.find_element_by_xpath(self.HIDDEN_INBOX_BUTTON)
        ActionChains(self.driver).move_to_element(nav_menu).click(hidden_inbox_button).perform()

    def open_letter(self, subject):
        letter = self.driver.find_element_by_xpath('//*[@class="bog"]/span[contains(.,"{}")]'.format(subject))
        letter.click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, EmailPage.LOGO_OF_SENDER)))

    def delete_last_letter(self):
        self.driver.find_element_by_xpath(self.LAST_LETTER_CHECKBOX).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.DELETE_BUTTON)))
        self.driver.find_element_by_xpath(self.DELETE_BUTTON)


class ComposePopUp(PageObject):

    subject_sender = 'Feeling'
    body_of_letter_sender = 'Hello! How are you?'

    # selectors
    COMPOSE_POP_UP = '//*[@class="AD"]'
    TO_FIELD = '//*[@name="to"]'
    SUBJECT_FIELD = '//*[@name="subjectbox"]'
    MESSAGE_BODY_FIELD = '//*[@class="Am Al editable LW-avf tS-tW"]'
    SEND_BUTTON = '//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]'

    # class methods
    def open_compose_pop_up(self):
        self.driver.find_element_by_xpath(InboxPage.COMPOSE_BUTTON).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, ComposePopUp.COMPOSE_POP_UP)))

    def fill_to_field(self, email):
        self.driver.find_element_by_xpath(self.TO_FIELD).send_keys(email)

    def fill_subject_field(self, subject):
        self.driver.find_element_by_xpath(self.SUBJECT_FIELD).send_keys(subject)

    def fill_body_of_letter(self, body):
        self.driver.find_element_by_xpath(self.MESSAGE_BODY_FIELD).send_keys(body)

    def click_send_button(self):
        send_button = self.driver.find_element_by_xpath(self.SEND_BUTTON)
        send_button.click()


class AccountPopUp(PageObject):

    # selectors
    ACCOUNT_BUTTON = '//*[@class="gb_ia gb_xg gb_i"]'
    ACCOUNT_POP_UP = '//*[@aria-label="Информация об аккаунте"]'
    SIGN_OUT_BUTTON = '//*[@id="gb_71"]'

    # class methods
    def open_account_information_pop_up(self):
        self.driver.find_element_by_xpath(self.ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, AccountPopUp.ACCOUNT_POP_UP)))

    def click_sign_out_button(self):
        self.driver.find_element_by_xpath(self.SIGN_OUT_BUTTON).click()
