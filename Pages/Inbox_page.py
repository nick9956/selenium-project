from Pages.Base_page import Page_Object
from selenium.webdriver.common.action_chains import ActionChains


class Inbox_page(Page_Object):

    # selectors
    COMPOSE_BUTTON = '//*[@class="T-I J-J5-Ji T-I-KE L3"]'
    NAV_MENU = '//*[@class="nH oy8Mbf nn aeN bhZ"]'
    HIDDEN_INBOX_BUTTON = '//*[@class="J-Ke n0" and @tabindex="0"]'

    # class methods
    def open_inbox_page(self):
        nav_menu = self.driver.find_element_by_xpath(self.NAV_MENU)
        hidden_inbox_button = self.driver.find_element_by_xpath(self.HIDDEN_INBOX_BUTTON)
        ActionChains(self.driver).move_to_element(nav_menu).click(hidden_inbox_button).perform()

    def open_letter(self):
        letter = self.driver.find_element_by_xpath('//*[@class="bog"]/span[contains(.,"Feeling")]')
        letter.click()


class Compose_pop_up(Page_Object):

    email = 'mykola.rudym@nure.ua'
    password = "2203Rudim1712"
    subject_sender = 'Feeling'
    body_of_letter_sender = 'Hello! How are you?'

    # selectors
    COMPOSE_POP_UP = '//*[@class="AD"]'
    TO_FIELD = '//*[@name="to"]'
    SUBJECT_FIELD = '//*[@name="subjectbox"]'
    MESSAGE_BODY_FIELD = '//*[@class="Am Al editable LW-avf tS-tW"]'
    SEND_BUTTON = '//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]'

    #class methods
    def open_compose_pop_up(self):
        self.driver.find_element_by_xpath(Inbox_page.COMPOSE_BUTTON).click()

    def fill_to_field(self):
        self.driver.find_element_by_xpath(self.TO_FIELD).send_keys(self.email)

    def fill_subject_field(self):
        self.driver.find_element_by_xpath(self.SUBJECT_FIELD).send_keys(self.subject_sender)

    def fill_body_of_letter(self):
        self.driver.find_element_by_xpath(self.MESSAGE_BODY_FIELD).send_keys(self.body_of_letter_sender)

    def click_send_button(self):
        send_button = self.driver.find_element_by_xpath(self.SEND_BUTTON)
        send_button.click()

class Account_pop_up(Page_Object):

    #selectors
    ACCOUNT_BUTTON = '//*[@class="gb_B gb_Da gb_g"]'
    ACCOUNT_POP_UP = '//*[@class="gb_Sa gb_D gb_Ec"]'
    SIGN_OUT_BUTTON = '//*[@id="gb_71"]'

    #class methods
    def open_account_information_pop_up(self):
        self.driver.find_element_by_xpath(self.ACCOUNT_BUTTON).click()

    def click_sign_out_button(self):
        self.driver.find_element_by_xpath(self.SIGN_OUT_BUTTON).click()
