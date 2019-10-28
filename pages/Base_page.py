from selenium import webdriver as webdriver


class WebDriverFactory:

    @staticmethod
    def get_webdriver(browserName):
        if browserName == 'chrome':
            my_chrome_options = webdriver.ChromeOptions()
            my_chrome_options.add_argument("--start-maximized")
            chrome_driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe',
                                             chrome_options=my_chrome_options)

            return chrome_driver
        elif browserName == 'firefox':
            firefox_driver = webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
            firefox_driver.maximize_window()
            return firefox_driver
        elif browserName == 'ie':
            return webdriver.Ie()
        raise Exception("The " + browserName + " browser does not exist")


class Page_Object(object):

    def __init__(self, driver):
        self.driver = driver


class Chrome_alerts(Page_Object):

    def accept_alert(self):
        self.driver.switch_to.alert.accept()


class Users(object):

    users_list = [
        # valid user
        {'name': "Mykola", 'email': 'mykola.rudym@nure.ua', 'password': '2203Rudim1712'},

        # invalid user
        {'name': 'Mykolay', 'email': 'mykola.rudym@nure.uk', 'password': '2203Rudim1713'}]

    def get_email(self, name):
        for i in self.users_list:
            if i['name'] == name:
                return i['email']

    def get_password(self, name):
        for i in self.users_list:
            if i['name'] == name:
                return i['password']
