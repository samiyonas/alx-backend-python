seed = __import__("seed")

def stream_users_in_batches(batch_size):
    query = "SELECT * FROM user_data"
    connection = seed.connect_to_prodev()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            while True:
                batch = cursor.fetchmany(batch_size)

                if not batch:
                    break

                yield batch
    except Exception as e:
        print(f"failure while streaming users in batches: {e}")

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_by_age = []
        for row in batch:
            if row[-1] > 25:
                filtered_by_age.append(row)
        yield filtered_by_age
