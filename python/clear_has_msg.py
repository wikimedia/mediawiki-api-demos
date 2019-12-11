#!/usr/bin/python3

"""
    clear_has_msg.py

    MediaWiki API Demos
    Demo of `ClearHasMsg` module: Clear the hasmsg flag for the current user.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "clearhasmsg",
    "format": "json"
}

R = S.post(url=URL, data=PARAMS)
DATA = R.json()

print(DATA)
