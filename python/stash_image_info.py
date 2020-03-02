#!/usr/bin/python3

"""
    stash_image_info.py

    MediaWiki API Demos
    Demo of `Stashimageinfo` module: Return information for a stashed file.
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
# method, obtain credentials by first visiting
# https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
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
DATA = R.json()

# Step 3: Send a request to return information for a stashed file.
PARAMS_4 = {
    "action": "query",
    "format": "json",
    "prop": "stashimageinfo",
    "siifilekey": "124sd34rsdf567"
}

R = S.post(url=URL, data=PARAMS_4)
DATA = R.text

print(DATA)
