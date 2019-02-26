#!/usr/bin/python3

"""
    blocks.py

    MediaWiki Action API Code Samples
    Demo of `Blocks` module: GET requst to list recent blocks

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

print(DATA)
