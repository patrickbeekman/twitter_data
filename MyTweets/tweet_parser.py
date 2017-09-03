import tweepy
from tweepy import OAuthHandler
import json

def main(args=None):
    # The main routine
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
     
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
      
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.user_timeline).items(10):
        print(json.dumps(tweet._json))
    


if __name__ == "__main__":
    main()
