#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    langbacklinks.py

    MediaWiki API Demos
    Demo of `Langbacklinks` module: Get pages linking to a given language link

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "list": "langbacklinks",
    "lbltitle": "Test",
    "lbllang": "fr",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
