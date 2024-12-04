import telebot

class TelegramBot:
    def __init__(self, master):
        print("Telegram")
        self.master = master
        self.init_variables()

    def init_variables(self):
        self.token = self.master.token
        self.bot = telebot.TeleBot(self.token)

    def start_bot(self):
        print("Start Telegram Bot")

        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.bot.reply_to(message, "Hello")
            self.user_id = message.from_user.id 

        @self.bot.message_handler(func=lambda message: True)
        def echo(message):
            self.bot.reply_to(message, message.text)
        
        @self.bot.message_handler(commands=["stop"])
        def stop_bot_tg(message):
            self.bot.reply_to(message, "Stopping the bot...")
            self.stop_bot()  
            self.bot.stop_polling()  
            

        self.bot.polling()

    def stop_bot(self):
        print("Bot stopped")