#This file is partly auto-generated

#!/usr/bin/python3

"""
    feedwatchlist_other.py

    MediaWiki Action API Code Samples
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
DATA = R.json()

print(DATA)
