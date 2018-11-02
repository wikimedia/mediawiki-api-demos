#This file is partly auto-generated

#!/usr/bin/python3

"""
    parse.py

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse content of a page

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "parse",
    "page": "Pet door",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
