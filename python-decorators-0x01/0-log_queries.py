from setup import create_table
import sqlite3
import functools
from datetime import datetime


def log_queries(func):
    def wrapper(*args, **kwargs):
        print(f"{datetime.now()}: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    create_table(conn)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")