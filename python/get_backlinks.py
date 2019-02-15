#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_backlinks.py

    MediaWiki Action API Code Samples
    Demo of `Backlinks` module: Get request to list pages which link to a certain page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "backlinks",
    "bltitle": "philosophy"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
