import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect('users.db')
            return func(conn, *args, **kwargs)
        except Exception:
            conn.close()
            raise
    return wrapper

def cache_query(func):
    def wrapper(*args, **kwargs):
        try:
            query_cache[kwargs.get('query')] = func(*args, **kwargs)
            return query_cache[kwargs.get('query')] 
        except Exception:
            raise
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(query_cache)
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(query_cache)