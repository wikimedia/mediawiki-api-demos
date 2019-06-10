#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_watchlistraw.py

    MediaWiki API Demos
    Demo of `Watchlistraw` module: Get three pages on the logged-in user's
    watchlist from the main namespace.

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

# Step 2: Send a post request to log in. For this login
# method, Obtain bot credentials by visiting
# https://en.wikipedia.org/wiki/Special:BotPasswords/
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "login",
    "lgname": "username",
    "lgpassword": "password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

# Step 3: While logged in, get the watchlist
PARAMS_3 = {
    "action": "query",
    "list": "watchlistraw",
    "format": "json",
    "wrnamespace": "0",
    "wrlimit": "3"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

print(DATA)
