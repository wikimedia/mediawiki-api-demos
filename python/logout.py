#!/usr/bin/python3

"""
    logout.py

    MediaWiki API Demos
    Demo of `Logout` module: Log out and clear session data.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

# Send a POST request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action':"login",
    'lgname':"your_bot_username",
    'lgpassword':"your_bot_password",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)

# GET request to fetch CSRF token
PARAMS_2 = {
    "action":"query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

print( CSRF_TOKEN )

# Send a POST request to logout.
PARAMS_3 = {
    "action": "logout",
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

# Check weither the response is null or not
if DATA == {}:
    print("You have successfully logout.")