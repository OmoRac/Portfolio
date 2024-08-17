import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

def view_reviews():
    try:
        db_name = "games_reviews"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = """
                SELECT  game_id ,game_title, user_id, username, review_text, rating
                FROM reviews
                """

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()
        print("Access to the reviews has been accepted.")
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_review(game_id, game_title, user_id, username, review_text, rating):
    try:
        db_name = "games_reviews"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                INSERT INTO reviews (game_id, game_title, user_id, username, review_text, rating, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
                """
        values = (game_id, game_title, user_id, username, review_text, rating)
        cur.execute(query, values)
        db_connection.commit()
        cur.close()
        print("Review added successfully")
    except Exception:
        raise DbConnectionError("Failed to add review to DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")




def search_reviews_by_id(game_id):
    try:
        db_name = "games_reviews"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = """
                SELECT game_id, game_title, user_id, username, review_text, rating
                FROM reviews
                WHERE game_id = %s
                """
        cur.execute(query, (game_id,))
        result = cur.fetchall()  # list of tuples
        cur.close()
        return result
    except Exception:

        raise DbConnectionError("Failed to search data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
