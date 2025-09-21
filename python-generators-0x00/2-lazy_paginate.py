seed = __import__("seed")

def paginate_users(pagesize, offset):
    connection = seed.connect_to_prodev()
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (pagesize, offset))

            yield cursor.fetchall()
    except Exception as e:
        print(e)
    

def lazypaginate(pagesize):
    offset = 0

    while True:
        page = paginate_users(pagesize, offset)

        if not page:
            break

        yield page
        offset += pagesize