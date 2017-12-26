import base64
import requests

# The two necessary keys that should be in a different file
client_key = 'e0tEUlJW8x1fAJpRSSHk7ynRf'
client_secret = 'GPhS5h6ylPede6EPnui0M3pODZgznohbCDOqQRFHYjFGwk0AX5'

# Format the public:private and then encode using base64
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
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

print('response: ',auth_resp.status_code)

access_token = auth_resp.json()['access_token']

# Above is how to authorize and get an access token to make requests from the api
# Below is how to make requests to the api

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    'q': 'General Election',
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()

for x in tweet_data['statuses']:
    print(x['text'], '\n')


