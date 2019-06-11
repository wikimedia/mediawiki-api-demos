#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_tags.py

    MediaWiki API Demos
    Demo of `Tags` module: Get the first three change tags and their hitcounts.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "tags",
    "tgprop": "hitcount",
    "tglimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
