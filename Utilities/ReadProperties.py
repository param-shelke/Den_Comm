import configparser

config = configparser.ConfigParser()

# location of config file from configuration package
config.read(r'C:\Users\Prem\Python\PycharmProjects\Den_Comm\Configuration\config.ini')


class Readconfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
