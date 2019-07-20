#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allfileusages.py

    MediaWiki API Demos
    Demo of `allfileusage` module: List all file usages, including non-existing

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "afprefix": "Icon",
    "list": "allfileusages",
    "afprop": "ids|title",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

USAGES = DATA["query"]["allfileusages"]

for img in USAGES:
    print(img["title"])
