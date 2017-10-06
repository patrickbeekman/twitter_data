import tweepy
from tweepy import OAuthHandler
import json
import os
import pandas as pd
import numpy as np

def main(args=None):
    # The main routine
    keys = open('keys.txt', 'r')
    keys.readline() #skip the first line of comments
    consumer_key = keys.readline().rstrip()
    consumer_secret = keys.readline().rstrip()
    access_token = keys.readline().rstrip()
    access_secret = keys.readline().rstrip()
     
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    filename = 'tweets.json'
    most_recent_tweet = ""
    most_recent_saved_tweet = ""

    for tweet in tweepy.Cursor(api.user_timeline).items(1):
        most_recent_tweet = tweet._json

    if os.path.isfile(filename):
        most_recent_saved_tweet = open(filename, 'r').readline()

    if grab_id_dict(most_recent_tweet) != grab_id_string(most_recent_saved_tweet):
        os.remove(filename)
        write_tweets_timeline(filename, api)


def write_tweets_timeline(filename, api):
    print("Grabbing all of your tweets, this may take a minute...")
    with open(filename, 'a') as f:
        for tweet in tweepy.Cursor(api.user_timeline).items():
            json.dump(tweet._json, f)
            f.write("\n")


def grab_id_string(tweet):
    try:
        x = tweet.split(", ")[1]
        id = x.split(" ")[1]
        return int(id)
    except IndexError:
        return None


def grab_id_dict(tweet):
    return tweet["id"]

if __name__ == "__main__":
    main()
