#!/usr/bin/python3

"""
    get_redirects.py

    MediaWiki Action API Code Samples
    Demo of `Redirects` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'format':"json",
    'titles':"Main Page",
    'prop': "redirects"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
