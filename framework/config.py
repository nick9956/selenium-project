import configparser


class Parser:

    @staticmethod
    def read_valid_email():
        email_parser = configparser.ConfigParser()
        email_parser.read('../config.ini')
        return email_parser.get('valid_user', 'email')

    @staticmethod
    def read_valid_password():
        password_parser = configparser.ConfigParser()
        password_parser.read('../config.ini')
        return password_parser.get('valid_user', 'password')

    @staticmethod
    def read_chrome_path():
        chrome_path__parser = configparser.ConfigParser()
        chrome_path__parser.read('../config.ini')
        return chrome_path__parser.get('paths', 'chromedriver_path')

    @staticmethod
    def read_firefox_path():
        firefox_path__parser = configparser.ConfigParser()
        firefox_path__parser.read('../config.ini')
        return firefox_path__parser.get('paths', 'firefoxdriver_path')



