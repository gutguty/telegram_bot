from database import Database

class Master:
    def __init__(self):
        self.squlite_db = Database()  

if __name__ == "__main__":
    db = Master()