from telegram_block.telegram import TelegramBot

class Master:
    def __init__(self,mode):
        print("INIT MASTER")
        self.mode = mode
        print(self.mode)
        self.token = "7555575054:AAGF6QqrXJaC6Db9PRlyNd7fbeA-RLrKzQs"
        self.init_modules()
        self.start_modules()
        self.main_loop()
        self.stop_modules()

    def init_modules(self):
        self.telegram = TelegramBot(self)

    def start_modules(self) :
        self.telegram.start_bot()

    def main_loop(self):
        self.is_work = True
        while self.is_work:
            command = input()
            if command == 'stop':
                self.is_work=False

    def stop_modules(self): 
        self.telegram.stop_bot()