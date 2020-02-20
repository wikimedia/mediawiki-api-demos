#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_feed_recent_changes.py

    MediaWiki API Demos
    Demo of `Feedrecentchanges` module: Show recent changes as an RSS feed.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "feedrecentchanges",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.content

print(DATA)
