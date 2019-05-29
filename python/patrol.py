#!/usr/bin/python3

"""
    patrol.py

    MediaWiki API Demos
    Demo of `Patrol` module: Patrol a recent change
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

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

# Step 2: Send a POST request to log in. For this login
# method, obtain bot credentials by first visiting
# https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
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
DATA = R.json()

# Step 3: While logged in, retrieve a patrol token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "type":"patrol",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

PATROL_TOKEN = DATA["query"]["tokens"]["patroltoken"]

# Step 4: Send a POST request to patrol a recent change
PARAMS_4 = {
    "action": "patrol",
    "format": "json",
    "rcid":"437659",
    "token": PATROL_TOKEN
}

R = S.post(url=URL, data=PARAMS_4)
DATA = R.json()

print(DATA)
