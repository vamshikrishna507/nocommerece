import configparser

config = configparser.RawConfigParser()
config.read("/Users/vamshi/PycharmProjects/nocommereceApp/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('commoninfo', 'base_url')
        return url

    @staticmethod
    def getusername():
        username = config.get('commoninfo', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('commoninfo', 'password')
        return password




