#!/usr/bin/python3

"""
    get_all_deleted_revisions.py

    MediaWiki API Demos
    Demo of `alldeletedrevisions` module: List the all deleted revisions from User:Mahesh

    MIT License
"""
import requests

S = requests.Session()

URL = "https://www.thetestwiki.org/w/api.php"
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

# Step 3: Send a get request to get all the deleted revisions

PARAMS_2 = {
    "action": "query",
    "list": "alldeletedrevisions",
    "adruser": "Mahesh",
    "adrprop": "ids|user|comment",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

PAGES = DATA['query']['alldeletedrevisions']

for p in PAGES:
    print("Revision for Page " + p["title"])
    for adrev in p["revisions"]:
        print(adrev)
