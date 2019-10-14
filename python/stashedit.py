#!/usr/bin/python3

"""
    stashedit.py

    MediaWiki API Demos
    Demo of `stashedit` module: prepare an edit in shared cache

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

# Step 2: Send a post request to log in using the clientlogin method.
# import rights can't be granted using Special:BotPasswords
# hence using bot passwords may not work.
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "clientlogin",
    "username": "username",
    "password": "password",
    "format": "json",
    "loginreturnurl": "http://127.0.0.1:5000/",
    "logintoken": LOGIN_TOKEN
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

# Step 4: Send a POST request to prepare an edit in shared cache

PARAMS_4 = {
    "token":CSRF_TOKEN,
    "action":"stashedit",
    "title":"User:Zaycodes/Sandbox/API:Mergehistory",
    "section":"new",
    "sectiontitle":"testing stashedit",
    "text":"testing stashedit API",
    "contentmodel":"text",
    "contentformat":"text/plain",
    "baserevid":1,
    "format":"json"
    }

R = S.post(URL, data=PARAMS_4)
DATA = R.text

print(DATA)
