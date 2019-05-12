#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_user_watchlist_feed.py

    MediaWiki API Demos
    Demo of `Feedwatchlist` module: Get a watchlist feed from another user.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "feedwatchlist",
    "wlowner": "sample_user",
    "wltoken": "sample_watchlist_token"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.text

print(DATA)
