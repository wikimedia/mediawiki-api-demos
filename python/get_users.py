#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_users.py

    MediaWiki API Demos
    Demo of `Users` module: Get information about several users:
    [[1.2.3.4]], [[Catrope]], [[Vandal01]], and [[Bob]]

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "users",
    "ususers": "Catrope|Bob",
    "usprop": "blockinfo|groups|editcount|registration|emailable|gender"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

USERS = DATA["query"]["users"]

for u in USERS:
    print(str(u["name"]) + " has " + str(u["editcount"]) + " edits.")
