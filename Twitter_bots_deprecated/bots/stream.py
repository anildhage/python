import tweepy
import logging
from config import create_api
import json
import pdb


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class devTweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    # Creates file to write to, and appends tweets to it
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)
        

    def on_error(self, status):
        logger.error(status)

# Main Function

def main(keywords):
    api = create_api()
    tweets_listener = devTweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

    
# Insert terms to be tracked in main([]), arguments are string values held in a list
if __name__ == "__main__":
    main(['485visas', '485Visas','extend485', 'Extend485', '485visaextension', '485VisaExtension','strandedstudents', '485visa', '485Visa','letusbacktoaus', 
        'PeaceShouts', 'InternationalStudentsAustralia', 'LetUsBackToAus', 'peaceshouts', 'aus_int_student', 'NickMcKim', 'AlexHawkeMP', 'tomwconnell', 'extend485visas'])






# created_at : The time the status was posted.
# id : The ID of the status.
# id_str : The ID of the status as a string.
# text : The text of the status.
# entities : The parsed entities of the status such as hashtags, URLs etc.
# source : The source of the status.
# source_url : The URL of the source of the status.
# in_reply_to_status_id : The ID of the status being replied to.
# in_reply_to_status_id_str : The ID of the status being replied to in as a string.
# in_reply_to_user_id : The ID of the user being replied to.
# in_reply_to_user_id_str : The ID of the user being replied to as a string.
# in_reply_to_screen_name : The screen name of the user being replied to
# user : The User object of the poster of the status.
# geo : The geo object of the status.
# coordinates : The coordinates of the status.
# place : The place of the status.
# contributors : The contributors of the status.
# is_quote_status : Indicates whether the status is a quoted status or not.
# retweet_count : The number of retweets of the status.
# favorite_count : The number of likes of the status.
# favorited : Indicates whether the status has been favourited by the authenticated user or not.
# retweeted : Indicates whether the status has been retweeted by the authenticated user or not.
# possibly_sensitive : Indicates whether the status is sensitive or not.
# lang : The language of the status.