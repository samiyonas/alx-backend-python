seed = __import__("seed")

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (page_size, offset))
            return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    

def lazypaginate(pagesize):
    offset = 0

    while True:
        page = paginate_users(pagesize, offset)

        if not page:
            break

        yield page
        offset += pagesize