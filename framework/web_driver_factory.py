from framework.pages.base_page import PageObject
from selenium import webdriver as webdriver
from framework.config import Config


class WebDriverFactory(PageObject):

    @staticmethod
    def get_webdriver(browser_name):
        config = Config()
        if browser_name == 'chrome':
            my_chrome_options = webdriver.ChromeOptions()
            config = Config()
            my_chrome_options.add_argument("--start-maximized")
            chrome_driver = webdriver.Chrome(executable_path=config.chrome_path,
                                             chrome_options=my_chrome_options)
            return chrome_driver
        elif browser_name == 'firefox':
            firefox_driver = webdriver.Firefox(executable_path=config.firefox_path)
            firefox_driver.maximize_window()
            return firefox_driver
        elif browser_name == 'ie':
            return webdriver.Ie()
        raise Exception("The " + browser_name + " browser does not exist")