#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allrevisions.py

    MediaWiki Action API Code Samples
    Demo of `Allrevision` module: Enumerate pages that contain a given URL.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "arvprop": "ids|flags|timestamp",
    "arvuser": "Place holder",
    "list": "allrevisions",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
