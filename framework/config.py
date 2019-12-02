import configparser


class Config:

    def __init__(self):
        self.__parser = configparser.ConfigParser()
        self.__parser.read('../config.ini')

        self.valid_email = self.__parser.get('valid_user', 'email')
        self.valid_password = self.__parser.get('valid_user', 'password')
        self.chrome_path = self.__parser.get('paths', 'chromedriver_path')
        self.firefox_path = self.__parser.get('paths', 'firefoxdriver_path')
