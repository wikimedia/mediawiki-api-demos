#!/usr/bin/python3

"""
    rollback.py

    MediaWiki API Demos
    Demo of `rollback` module: Sending post request to rollback the
    last edits made to a given page.

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

# Step 2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_2 = {
    "action": "login",
    "lgname": "bot_user_name",
    "lgpassword": "bot_password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: POST request to edit a page
PARAMS_4 = {
    "action": "edit",
    "title": "Sandbox",
    "token": CSRF_TOKEN,
    "format": "json",
    "appendtext": "Hello"
}

R = S.post(URL, data=PARAMS_4)

# Step 5: Retrieve a rollback token
PARAMS_5 = {
    "action": "query",
    "meta": "tokens",
    "type": "rollback",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_5)
DATA = R.json()

ROLLBACK_TOKEN = DATA['query']['tokens']['rollbacktoken']

# Step 5: POST request to rollback a page
PARAMS_6 = {
    "action": "rollback",
    "format": "json",
    "title": "Sandbox",
    "user": "bot_user_name",
    "token": ROLLBACK_TOKEN,
}

R = S.post(URL, data=PARAMS_6)
DATA = R.json()

print(DATA)
