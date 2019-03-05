#!/usr/bin/python3

"""
    watchlist.py
    MediaWiki Action API Code Samples
    Demo of `Watchlist` module: getting current user's watchlist
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: GET Request to fetch login token
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST Request to log in. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    "action": "login",
    "lgname": "your_bot_username",
    "lgpassword": "your_bot_passwords",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: POST request to get the current user's watchlist
PARAMS_2 = {
    "action": "query",
    "list": "watchlist",
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)
DATA = R.json()

print(DATA)

