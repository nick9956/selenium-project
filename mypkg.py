from selenium.webdriver.chrome.webdriver import WebDriver

driver = None


def getOrCreateWebdriver():
    global driver
    driver = WebDriver(executable_path='C:/Users/Mykola_Rudym/Documents/selenium/chromedriver.exe')
    driver.maximize_window()
    return driver
