import tweepy
from tweepy import OAuthHandler
import json
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

    output_file = open('tweets.json', 'w')
    mylist = []

    for tweet in tweepy.Cursor(api.user_timeline).items(10):
        mylist.append(tweet._json)
    
    process_and_write(mylist, output_file)

def process_and_write(tweets, out_file):
    for item in tweets:
        out_file.write(json.dumps(item) + "\n")
    #out_file.write(json.dumps(tweet))

if __name__ == "__main__":
    main()
