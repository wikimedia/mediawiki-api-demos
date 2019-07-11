#!/usr/bin/python3

"""
    create_account.py

    MediaWiki API Demos
    Demo of `createaccount` module: Create an account on a wiki without the
    special authentication extensions

    MIT license
"""

import requests

S = requests.Session()

WIKI_URL = "http://dev.wiki.local.wmftest.net:8080"
API_ENDPOINT = WIKI_URL + "/w/api.php"

# First step
# Retrieve account creation token from `tokens` module

PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"createaccount",
    'format':"json"
}

R = S.get(url=API_ENDPOINT, params=PARAMS_0)
DATA = R.json()

TOKEN = DATA['query']['tokens']['createaccounttoken']

# Second step
# Send a post request with the fetched token and other data (user information,
# return URL, etc.)  to the API to create an account

PARAMS_1 = {
    'action': "createaccount",
    'createtoken': TOKEN,
    'username': 'your_username',
    'password': 'your_password',
    'retype': 'retype_your_password',
    'createreturnurl': WIKI_URL,
    'format': "json"
}

R = S.post(API_ENDPOINT, data=PARAMS_1)
DATA = R.json()

print(DATA)
