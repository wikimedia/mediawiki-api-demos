#!/usr/bin/python3

"""
    undelete.py

    MediaWiki API Demos
    Demo of `Undelete` module: Restore two revisions of a deleted page

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

# Step 2: Send a post request to login.
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

# Step 3: While logged in, get an CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a post request to restore two revisions of a deleted page
PARAMS_4 = {
    "action": "undelete",
    "format": "json",
    "token": CSRF_TOKEN,
    "title": "Sandbox/Test",
    "timestamps":"20190605072148|20190605074313",
    "reason": "Test undeleting via the API"
}

R = S.post(URL, data=PARAMS_4)
DATA = R.json()

print(DATA)
