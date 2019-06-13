#!/usr/bin/python3

"""
    assert_user.py

    MediaWiki API Demos
    Demo of `Assert` module: Check whether a user is logged in

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: Send a POST request to login.
# Obtain credentials for lgname & lgpassword via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords)
PARAMS_2 = {
    "action": "login",
    "lgname": "username",
    "lgpassword": "password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)

# Send a GET request to assert that the user is logged-in
PARAMS_3 = {
    'action':"query",
    'format':"json",
    'assert':"user"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

print(DATA)
