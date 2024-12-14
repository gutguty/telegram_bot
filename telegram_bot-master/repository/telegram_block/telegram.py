import telebot
from database_block.database import Database
import threading

class TelegramBot:
    def __init__(self, master, database):
        print("Telegram")
        self.master = master 
        self.database = database
        self.init_variables() 
        self.stop_event = threading.Event()
        self.bot_thread = threading.Thread(target=self.start_bot)
        self.bot_thread.start()        

    def init_variables(self):
        self.token = "7555575054:AAGF6QqrXJaC6Db9PRlyNd7fbeA-RLrKzQs" 
        self.bot = telebot.TeleBot(self.token)

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

    def start_bot(self):
        print("Start Telegram Bot")
        while not self.stop_event.is_set():
            try:
                self.bot.polling(none_stop=True)
            except Exception as e:
                print(f"Error in polling: {e}")
                break

    def stop_bot(self):
        self.stop_event.set() 
        self.database.close()   
        self.bot.stop_polling()  
        print("Bot stopped")