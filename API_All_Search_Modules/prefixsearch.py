#!/usr/bin/python3

"""
    prefixsearch.py

    MediaWiki Action API Code Samples
    Demo of `Prefixsearch` module: Perform a prefix search for page titles
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHTERM = "Star Wars"

PARAMS = {
    'action':"query",
    'list':"prefixsearch",
    'pssearch':SEARCHTERM,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
