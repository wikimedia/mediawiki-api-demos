#!/usr/bin/python3

"""
    get_exturlusage.py

    MediaWiki Action API Code Samples
    Demo of `Exturlusage` module: Enumerate pages that contain a given URL:
    [slashdot.org]

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "exturlusage",
    "euquery": "slashdot.org"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
