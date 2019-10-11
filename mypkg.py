from selenium import webdriver


def getOrCreateWebdriver():
    driver = webdriver.Chrome(executable_path='C:/Users/Mykola_Rudym/selenium-project/Drivers/chromedriver.exe')
    driver.maximize_window()
    return driver
