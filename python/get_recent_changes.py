#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_recent_changes.py

    MediaWiki API Demos
    Demo of `RecentChanges` module: Get the three most recent changes with
    sizes and flags

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "format": "json",
    "rcprop": "title|ids|sizes|flags|user",
    "list": "recentchanges",
    "action": "query",
    "rclimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RECENTCHANGES = DATA['query']['recentchanges']

for rc in RECENTCHANGES:
    print(str(rc['title']))
