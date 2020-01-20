#!/usr/bin/python3

"""
    revision_delete.py

    MediaWiki API Demos
    Demo of `Revisiondelete` module: Hide all information about a certain revision ID. 
    (The target, Sample Page, is unnecessary in this case.)

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

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a POST request to hide all information about a certain revision ID. 
# (The target, Sample Page, is unnecessary in this case.)
PARAMS_4 = {
    "action":"revisiondelete",
    "type":"revision",
    "ids":"71",
    "format":"json",
    "hide":"content|comment|user",
    "reason":"Because",
    "token" : CSRF_TOKEN
    }

R = S.post(URL, data=PARAMS_4)
DATA = R.text

print(DATA)
