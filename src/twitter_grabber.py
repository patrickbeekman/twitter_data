'''
twitter_grabber.py
A direct way to access the twitter RESTful api to grab twitter data for further data analysis.
'''
import base64
import requests
import os
import pandas as pd
import numpy as np

base_url = 'https://api.twitter.com/'

def main(args=None):
    bearer_token = authorize('keys.txt')
    if bearer_token is not None:
        tweets = get_usertimeline(bearer_token, 'grauson420')
        write_to_file('graysons_tweets.txt', tweets)

    '''
    if bearer_token != None:
        search_params = {
            'q': 'General Election',
            'result_type': 'recent',
            'count': 15
        }
        tweet_data = query(bearer_token, search_params, '1.1/search/tweets.json')
    '''


def get_usertimeline(token, username):
    search_params = {
        'screen_name': str(username),
        'count': 100
    }
    tweet_data = query(token, search_params, '1.1/statuses/user_timeline.json')
    len_new = 100
    while len_new >= 1:
        print(str(len(tweet_data)))
        search_params = {
            'screen_name': str(username),
            'since_id': tweet_data[len(tweet_data)-1]['id'],
            'count': 100
        }
        new_data = query(token, search_params, '1.1/statuses/user_timeline.json')
        len_new = len(new_data)
        tweet_data += new_data

    return tweet_data


def write_to_file(filename, data):
    file = open(filename, 'a')
    for x in data:
        file.write(x['text'] + '\n')


def query(bearer_tok, params, endpoint):
    '''
    query: Performs a query on the twitter RESTful api using params and an endpoint
    :param bearer_tok: The bearer token that we got from a successful authorization
    :param params: A map object of the parameters we will be on the api
    :param endpoint: The endpoint location we will access on the api
    :return: All the requested information in json format
    '''
    headers = {
        'Authorization': 'Bearer {}'.format(bearer_tok)
    }

    api_path = base_url + endpoint
    resp = requests.get(api_path, headers=headers, params=params)

    if check_status(resp.status_code):
        tweet_data = resp.json()
        return tweet_data
    else:
        return None
 
def check_status(status_code):
    '''
    check_status: Checks whether the response status is successful or not
    :param status_code: The status code we are checking
    :return: True if it is 200 (aka. successful) False otherwise and print an error message
    '''
    if status_code == 200:
        return True
    else:
        print('Error: authorization failed with status ' + str(status_code))
        return False

def authorize(filename):
    '''
    authorize: Authorizes the user application and connects to the RESTful twitter api
    :param filename: The name of the file containing the public/private keys this file should
                     have a single line of documentation \n public key \n private key
    :return: The bearer token for api requests
    '''
    keys_file = open(filename, 'r')
    keys_file.readline() # skip the first line of comments
    public_key = keys_file.readline().rstrip()
    private_key = keys_file.readline().rstrip()
   
    # Format the public:private and then encode using base64
    key_secret = '{}:{}'.format(public_key, private_key).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    # twitter api url
    base_url = 'https://api.twitter.com/'
    # the authorization endpoint
    auth_url = '{}oauth2/token'.format(base_url)

    # Header info for the authorization
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    # Was the authorization successful (aka. 200)
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    if check_status(auth_resp.status_code):
        return auth_resp.json()['access_token']
    else:
        return None

if __name__ == "__main__":
    main()
