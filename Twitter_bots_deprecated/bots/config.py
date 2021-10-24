import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    # TR485Graduate = tweepy.Stream('CONSUMER_KEY_485', 'CONSUMER_SECRET_485', 'ACCESS_TOKEN_485','ACCESS_TOKEN_SECRET_485' )
    consumer_key = os.getenv("CONSUMER_KEY_485")
    consumer_secret = os.getenv("CONSUMER_SECRET_485")
    access_token = os.getenv("ACCESS_TOKEN_485")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET_485")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise Exception
    logger.info("API created")
    return api


