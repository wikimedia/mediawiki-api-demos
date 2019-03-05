#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_blocked_users.py

    MediaWiki Action API Code Samples
    Demo of `Blocks` module: GET request to list recent blocked users

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "bklimit": "3",
    "list": "blocks",
    "bkprop": "id|user|by|timestamp|expiry|reason|range|flags",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['query']['blocks'])
