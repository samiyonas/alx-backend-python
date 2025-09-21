from mysql.connector import connect
import csv
import uuid

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "adminpassword"
DB = "ALX_prodev"

def connect_db():
    try:
        connection = connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD
        )

        return connection
    except Exception:
        print("connection mysql failed")
        return None


def create_database(connection):
    query = f"CREATE DATABASE IF NOT EXISTS {DB}"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print("can't create db")
        return None

def connect_to_prodev():
    try:
        connection = connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB
        )

        return connection
    except Exception:
        print("connection to db failed")
        return None


def create_table(connection):
    query = """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(128) NOT NULL,
                email VARCHAR(128) NOT NULL,
                age DECIMAL NOT NULL
            );
        """
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except Exception:
        print("failed to create table user_data")


def insert_data(connection, data):
    query = """
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s);
        """
    cursor = connection.cursor()
    try:
        with open(data, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
            
                cursor.execute(query, (user_id, name, email, age))
            
            connection.commit()
        print("csv data inserted successfully")
    except FileNotFoundError:
        print("csv file not found")
    except Exception:
        print("mysql error happened")
    finally:
        cursor.close()
