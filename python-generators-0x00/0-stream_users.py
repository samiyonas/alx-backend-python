seed = __import__("seed")

def stream_users():
    connection = seed.connect_db()
    query = "SELECT * FROM user_data"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            for row in cursor:
                yield row
    except Exception as e:
        print(e)