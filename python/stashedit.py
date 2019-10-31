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
CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a POST request to prepare an edit in shared cache

PARAMS_4 = {
    "token":CSRF_TOKEN,
    "action":"stashedit",
    "section":"new",
    "sectiontitle":"testing stashedit",
    "text":"testing stashedit API",
    "contentmodel":"wikitext",
    "contentformat":"text/x-wiki",
    "baserevid":"",
    "format":"json"
}