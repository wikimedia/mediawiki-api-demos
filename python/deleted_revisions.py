#!/usr/bin/python3

"""
    deleted_revisions.py

    MediaWiki API Demos
    Demo of `Deletedrevisions` module: Get a list of deleted revisions for Talk:Main Page.

    MIT License
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

# Step 3: While logged in, send a get reguest to get a list of deleted revisions for Talk:Main Page.
PARAMS = {
    "action": "query",
    "titles": "Talk:Main_Page",
    "prop": "deletedrevisions",
    "drvprop": "user|comment|content",
    "drvslots": "*",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
