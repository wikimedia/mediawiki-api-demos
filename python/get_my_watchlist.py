#!/usr/bin/python3

"""
    get_my_watchlist.py

    MediaWiki Action API Code Samples
    Demo of `Feedwatchlist` module: Get the watchlist feed 
    for the account making the request.
    MIT license
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

# Step 2: Send a post request to log in. For this login 
# method, Obtain credentials by first visiting
# https://en.wikipedia.org/wiki/Special:BotPasswords/
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "login",
    "lgname": "user_name",
    "lgpassword": "password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

# Step 3: Request the account's own watchlist feed
PARAMS_3 = {
    "action": "feedwatchlist"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.text

print(DATA)
