seed = __import__("seed")

def stream_user_ages():
    query = "SELECT age FROM user_data"
    connection = seed.connect_to_prodev()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            
            for (age,) in cursor:
                yield age
    except Exception as e:
        print(e)
        return 0


def avg_age():
    counter = 0
    age_sum = 0

    for age in stream_user_ages():
        age_sum += age
        counter += 1

    return age_sum / counter