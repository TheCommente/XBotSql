# services/tweet_manager.py

from config.database import connect_to_db

def get_unposted_tweet(connection):
    """
    Retrieves an unposted tweet from the database.
    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection object.
    Returns:
        dict: A dictionary containing the tweet details or None if no unposted tweet is found.
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tweets WHERE posted = FALSE LIMIT 1")
    tweet = cursor.fetchone()
    cursor.close()
    return tweet

def mark_as_posted(connection, tweet_id):
    """
    Marks a tweet as posted in the database.
    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection object.
        tweet_id (int): The ID of the tweet to be marked as posted.
    """
    cursor = connection.cursor()
    cursor.execute("UPDATE tweets SET posted = TRUE WHERE id = %s", (tweet_id,))
    connection.commit()
    cursor.close()

def reset_all_tweets(connection):
    """
    Resets all tweets in the database to unposted.
    Args:
        connection (mysql.connector.connection.MySQLConnection): The database connection object.
    """
    cursor = connection.cursor()
    cursor.execute("UPDATE tweets SET posted = FALSE")
    connection.commit()
    cursor.close()
    print("All tweets have been reset to unposted.")
