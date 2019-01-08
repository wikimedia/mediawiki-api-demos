#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_random.py

    MediaWiki Action API Code Samples
    Demo of `Random` module: Get request to list 5 random pages.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "5"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
