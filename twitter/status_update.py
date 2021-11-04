import tweepy

consumer_key =""
consumer_secret= ""
access_token=""
access_token_secret=""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("#INDvsNZ, Who is in form?")