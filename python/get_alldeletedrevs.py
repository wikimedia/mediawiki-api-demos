#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_alldeletedrevs.py

    MediaWiki API Demos
    Demo of `alldeletedrevisions` module: List the all deleted revisions from User

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "list": "alldeletedrevisions",
    "adruser": "Mahesh",
    "adrprop": "ids|user|comment",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
