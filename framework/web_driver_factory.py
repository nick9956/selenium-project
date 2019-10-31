from framework.pages.base_page import PageObject
from selenium import webdriver as webdriver
from framework.config import Parser


class WebDriverFactory(PageObject):

    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'chrome':
            my_chrome_options = webdriver.ChromeOptions()
            my_chrome_options.add_argument("--start-maximized")
            chrome_driver = webdriver.Chrome(executable_path=Parser.read_chrome_path(),
                                             chrome_options=my_chrome_options)

            return chrome_driver
        elif browser_name == 'firefox':
            firefox_driver = webdriver.Firefox(executable_path=Parser.read_firefox_path())
            firefox_driver.maximize_window()
            return firefox_driver
        elif browser_name == 'ie':
            return webdriver.Ie()
        raise Exception("The " + browser_name + " browser does not exist")