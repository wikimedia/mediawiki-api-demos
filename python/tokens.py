#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    tokens.py

    MediaWiki API Demos
    Demo of `Token` module: Fetch token of type `login`

    MIT License
"""

import requests

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)
