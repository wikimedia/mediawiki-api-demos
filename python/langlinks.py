#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    langlinks.py

    MediaWiki API Demos
    Demo of `Langlinks` module: Get a list of language links that a given page has

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Albert Einstein",
    "prop": "langlinks",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
