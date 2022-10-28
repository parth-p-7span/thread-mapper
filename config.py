import tweepy
import logging
import requests
import constants

logger = logging.getLogger()


# returns tweepy Client
def create_client():
    consumer_key = constants.CONSUMER_KEY
    consumer_secret = constants.CONSUMER_SECRET
    access_token = constants.ACCESS_TOKEN
    access_token_secret = constants.ACCESS_TOKEN_SECRET
    bearer_token = constants.BEARER_TOKEN

    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret,
                           return_type=requests.Response,
                           wait_on_rate_limit=True)
    return client


# returns tweepy API
def create_api():
    auth = tweepy.OAuthHandler(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
    auth.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api
