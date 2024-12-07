import sqlite3
#foreign key - внешний ключ (на id на который ссылаемся)
#primary key - первичный ключ
class Database:
    def __init__(self):
        print("INIT DATABASE")

        
        
        self.connection = sqlite3.connect('Database_tg.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            chat_id INTEGER,
            username TEXT NOT NULL,
            message TEXT NOT NULL)
        ''')
        self.connection.commit()
        self.clear_users_table()

    def clear_users_table(self):
        self.cursor.execute("DELETE FROM Users")
        self.connection.commit()
        print("Users table cleared.")



    def insert_user(self, user_id, username, message):
        
        self.cursor.execute("INSERT INTO Users (chat_id, username, message) VALUES (?, ?, ?)", 
                            (user_id, username, message))
        self.connection.commit()
        
    
    def close(self):
        self.connection.close()

    def insert_user_from_message(self, message):
        user_id = message.from_user.id
        username = message.from_user.username
        user_message = message.text
        self.insert_user(user_id, username, user_message)
        self.connection.commit()
        print("Insert successfully")
