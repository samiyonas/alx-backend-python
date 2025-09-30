import sqlite3

class ExecuteQuery:
    def __init__(self, query="SELECT * FROM users WHERE age > ?", para=25):
        self.db_obj = sqlite3.connect('users.db')
        self.query = query
        self.para = para
        self.cursor = ""
        self.result = ""
    
    def __enter__(self):
        try:
            self.cursor = self.db_obj.cursor()
            self.cursor.execute(self.query, (self.para))
            self.result = self.cursor.fetchall()
        except Exception as e:
            print(f"db error: {e}")

        return self 
    def __exit__(self, exc_type, exc_val, traceback):
        if self.cursor:
            self.cursor.close()
        self.db_obj.close()