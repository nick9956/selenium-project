from selenium import webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait


class WebDriverFactory:

    @staticmethod
    def get_webdriver(browserName):
        if browserName == 'chrome':
            my_chrome_options = webdriver.ChromeOptions()
            my_chrome_options.add_argument("--start-maximized")
            chrome_driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe',
                                             chrome_options=my_chrome_options)

            return chrome_driver
        elif browserName == 'firefox':
            firefox_driver = webdriver.Firefox(executable_path='./Drivers/geckodriver.exe')
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
