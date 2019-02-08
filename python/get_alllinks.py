#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_alllinks.py

    MediaWiki Action API Code Samples
    Demo of `Alllinks` module: List links pointing to the given namespace.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "alllinks",
    "alnamespace": "0",
    "alunique": "1"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
