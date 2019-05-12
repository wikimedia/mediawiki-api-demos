#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_deleted_revisions.py

    MediaWiki API Demos
    Demo of `Deletedrevs` module: List the six most recent deleted revisions from User:Catrope

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "drend": "20070904000000",
    "format": "json",
    "druser": "Catrope",
    "list": "deletedrevs",
    "drstart": "20070904235959",
    "drlimit": "6",
    "drprop": "revid|user|minor|len|token",
    "action": "query"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
