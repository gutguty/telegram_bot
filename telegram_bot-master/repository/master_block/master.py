from telegram_block.telegram import TelegramBot
from database_block.database import Database

class Master:
    def __init__(self):
        print("INIT MASTER")
        self.init_modules()


    def init_modules(self):
        self.database = Database()
        self.telegram = TelegramBot(self,self.database)
        

    