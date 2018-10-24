#!/usr/bin/python3

"""
   get_two_random_pages.py

    MediaWiki Action API Code Samples
    Demo of `Random` module: get two random pages
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnnamespace": "0",
    "rnlimit": "2"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.text

print(DATA)
