import telebot
from database_block.database import Database

class TelegramBot:
    def __init__(self, master):
        print("Telegram")
        self.master = master  
        self.init_variables()
        self.database = Database() 
        self.start_bot()

    def init_variables(self):
        self.token = "7555575054:AAGF6QqrXJaC6Db9PRlyNd7fbeA-RLrKzQs" 
        self.bot = telebot.TeleBot(self.token)

    def start_bot(self):
        print("Start Telegram Bot")
        self.running = True

        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.bot.reply_to(message, "Hello")
            self.database.insert_user_from_message(message)

        @self.bot.message_handler(commands=["stop"])
        def stop_bot_tg(message):
            self.bot.reply_to(message, "Stopping the bot...")
            self.stop_bot()

        @self.bot.message_handler(func=lambda message: True)
        def echo(message):
            self.bot.reply_to(message, message.text)
            self.database.insert_user_from_message(message)

        self.bot.polling()

    def stop_bot(self):
        if self.running:
            print("Stopping the bot...")
            self.bot.stop_polling()  
            self.running = False  
            print("Bot stopped")
            self.database.close()  
