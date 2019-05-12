#!/usr/bin/python3

"""
    watch.py

    MediaWiki API Demos
    Demo of `Watch` module: Add a page to your watchlist
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

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# Step 2: Send a post request to log in. For this login
# method, Obtain credentials by first visiting
# https://www.en.wikipedia.org/wiki/Special:BotPasswords
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

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "type": "watch",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["watchtoken"]

# Step 4: Post request to add a page to your watchlist
PARAMS_4 = {
    "action": "watch",
    "titles": "Stone forest",
    "format": "json",
    "token": CSRF_TOKEN,
}

R = S.post(URL, data=PARAMS_4)
DATA = R.json()

print(DATA)
