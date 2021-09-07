import configparser as  cp
config = cp.RawConfigParser()

config.read(".\\configfiles\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'USERNAME')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'PASSWORD')
        return password