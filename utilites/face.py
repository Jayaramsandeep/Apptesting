import configparser
face = configparser.RawConfigParser()
face.read(".\\Configuration\\face.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = face.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = face.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = face.get('common info', 'password')
        return password