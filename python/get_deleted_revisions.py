#!/usr/bin/python3

"""
    get_deleted_revisions.py

    MediaWiki API Demos
    Demo of `Deletedrevs` module: List the six most recent deleted revisions from User:Catrope

    MIT License
"""

import requests

S = requests.Session()

URL = "http://dev.wiki.local.wmftest.net:8080/w/api.php"

# Step1: Retrieve login token
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    'action':"login",
    'lgname':"your_bot_username",
    'lgpassword':"your_bot_password",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: Send a get request to get the deleted revisions

PARAMS_2 = {
    "action": "query",
    "list": "deletedrevs",
    "druser": "Catrope",
    "drprop": "revid|user|minor|len|token",
    "drlimit": "6",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

PAGES = DATA['query']['deletedrevs']

for p in PAGES:
    print("Revision for Page " + p["title"])
    for drev in p["revisions"]:
        print(drev)
