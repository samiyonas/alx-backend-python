import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.db_obj = sqlite3.connect('users.db')
    
    def __enter__(self):
        return self.db_obj

    def __exit__(self, exc_type, exc_val, trackback):
        self.db_obj.close()


with DatabaseConnection() as conn:
    query = "SELECT * FROM users"

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print(f"database error: {e}")
        raise Exception
    finally:
        cursor.close()