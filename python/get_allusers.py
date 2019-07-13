#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allusers.py

    MediaWiki API Demos
    Demo of `Allusers` module: Get all users, starting from those whose name
    begins with the string, 'Drov'.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allusers",
    "auprefix": "Drov"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

USERS = DATA["query"]["allusers"]

for user in USERS:
    print(user["name"])
