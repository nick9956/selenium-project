from framework.web_driver_factory import WebDriverFactory
from framework.pages.chrome_alerts import ChromeAlerts
from framework.pages.email_page import EmailPage
from framework.pages.inbox_page import *
from framework.pages.sign_in_email_page import *
from framework.pages.sign_in_password_page import *
from framework.pages.sign_out_page import *
from framework.config import *


class Application(object):

    config = Config()

    driver = WebDriverFactory.get_webdriver(config.chrome)

    account_pop_up = AccountPopUp(driver)

    chrome_alerts = ChromeAlerts(driver)

    email_page = EmailPage(driver)

    inbox_page = InboxPage(driver)

    signin_email_page = SignInEmailPage(driver)

    signin_password_page = SignInPasswordPage(driver)

    compose_pop_up = ComposePopUp(driver)

    signout_page = Signout_page(driver)



