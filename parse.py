#!/usr/bin/python3

"""
    parse.py

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse content of a page
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

TITLE = "Pet door"

PARAMS = {
    'action': "parse",
    'page': TITLE,
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
