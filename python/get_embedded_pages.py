#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_embedded_lists.py

    MediaWiki API Demos
    Demo of `Embeddedin` module: Get all page(s) that
    embed a given page

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "embeddedin",
    "eititle": "Computer",
    "eilimit": "20"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["embeddedin"]

for p in PAGES:
    print(p["title"])
