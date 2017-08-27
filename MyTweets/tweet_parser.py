import tweepy
from tweepy import OAuthHandler
import json

def main(args=None):
    # The main routine
    consumer_key = 'e0tEUlJW8x1fAJpRSSHk7ynRf'
    consumer_secret = 'GPhS5h6ylPede6EPnui0M3pODZgznohbCDOqQRFHYjFGwk0AX5'
    access_token = '319943657-R90Uu0oUZ9Twf4Gmv7K5auqWHzr2p7QGb8yPHOAF'
    access_secret = 'M4zl9SkOkma1iLLTpSzahpx62l6tvGiaTynmEREGE8I3g'
     
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
      
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.user_timeline).items(10):
        print(json.dumps(tweet._json))
    


if __name__ == "__main__":
    main()
