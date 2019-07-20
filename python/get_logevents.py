#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_logevents.py

    MediaWiki API Demos
    Demo of `Logevents` module: Get the three most recent logevents.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "logevents",
    "lelimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

LOGS = DATA["query"]["logevents"]

for l in LOGS:
    print("There is " + l["type"] + " log for page " + l["title"])
