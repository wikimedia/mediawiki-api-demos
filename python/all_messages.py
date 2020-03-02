#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    all_messages.py

    MediaWiki API Demos
    Demo of `Allmessages` module: Get the Dutch translations of some messages

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "allmessages",
    "ammessages": "august|mainpage|edit|rollback-success",
    "amlang": "nl",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
