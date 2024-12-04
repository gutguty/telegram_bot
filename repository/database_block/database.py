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
            chat_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            message TEXT NOT NULL)
        ''')
        self.connection.commit()

    def insert_user(self, user_id, username, message):
        # Проверяем, существует ли пользователь
        user = self.cursor.execute("SELECT * FROM Users WHERE chat_id = ?", (user_id,)).fetchone()
        if not user:
            self.cursor.execute("INSERT INTO Users (chat_id, username, message) VALUES (?, ?, ?)", 
                                (user_id, username, message))
            self.connection.commit()
        else:
            print(f"User with chat_id {user_id} already exists.")

    def close(self):
        self.connection.close()