import os

#export NY_VAR='123' fol linux and mac
#set MY_VAR='123' #for windows

class Enviroment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/api_dev',
        PROD: 'https://playground.learnqa.ru/api'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
            print(f"ENV variable found: {self.env}")  # Отладочная печать
        except KeyError:
            self.env = self.DEV
            print(f"ENV variable not found: {self.env}")  # Отладочная печать

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


ENV_OBJECT = Enviroment()