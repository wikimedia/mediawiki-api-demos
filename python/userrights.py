#!/usr/bin/python3

"""
    userrights.py

    MediaWiki Action API Code Samples
    Demo of `Userrights` module: Add and remove user rights by 
    changing the user's group membership.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Step 1: Obtain Userrights token

PARAMS_1 = {
    "action":"query",
    "format":"json",
    "meta":"tokens",
    "type":"userrights"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

USERRIGHTS_TOKEN = DATA["query"]["tokens"]["userrightstoken"]

# Step 2: Request user has group membership added and removed

PARAMS_2 = {
    "action":"userrights",
    "format":"json",
    "user":"Bob",
    "add":"sysop",
    "remove":"bureaucrat",
    "reason":"Oops, put Bob in the wrong group",
    "token":USERRIGHTS_TOKEN
}

HEADERS = {"token":USERRIGHTS_TOKEN}

R = S.post(URL, data=PARAMS_2, headers=HEADERS)

DATA = R.json()

print(DATA)