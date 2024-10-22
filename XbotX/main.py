# main.py

from services.twitter_service import create_driver, login_to_twitter, tweet_with_image
from services.tweet_manager import get_unposted_tweet, mark_as_posted, reset_all_tweets
from config.database import connect_to_db

def main():
    # Connect to the database
    connection = connect_to_db()
    driver = create_driver()

    try:
        # Log in to Twitter
        login_to_twitter(driver)

        # Keep posting tweets until all have been posted
        while True:
            tweet = get_unposted_tweet(connection)
            if tweet:
                tweet_with_image(driver, tweet["content"], tweet.get("image_path"))
                mark_as_posted(connection, tweet["id"])
            else:
                print("No unposted tweets found. Resetting all tweets to unposted.")
                reset_all_tweets(connection)
                continue  # Restart the loop to start posting tweets again
    finally:
        connection.close()
        driver.quit()

if __name__ == "__main__":
    main()
