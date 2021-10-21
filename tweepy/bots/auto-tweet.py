import tweepy
import logging
from config import create_api
import time
import random
import pdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

random_posts = ['post1', 'post2', 'post3', 'post4', 'post5']

def auto_tweet(api):
    random_post = random.choice(random_posts)
    api.update_status(random_post)

def main():
    api = create_api()
    while True:
        auto_tweet(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()