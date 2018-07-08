#!/usr/bin/python3

"""
    tokens.py

    MediaWiki Action API Code Samples
    Demo of `Token` module: Fetch token of type `login`
    MIT license
"""

import requests

S = requests.Session()

URL = "https://mediawiki.org/w/api.php"

PARAMS = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)
