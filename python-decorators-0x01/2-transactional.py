import sqlite3 
import functools

"""your code goes here"""
def with_db_connection(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect('users.db')
            return func(conn, *args, **kwargs)
        except Exception:
            raise
    return wrapper

def transactional(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            args[0].rollback()
        else:
            args[0].commit()
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')