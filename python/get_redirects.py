#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_redirects.py

    MediaWiki API Demos
    Demo of `Redirects` module: Get all redirects to the given page(s)

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Jacques Kallis",
    "prop": "redirects"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    for re in v["redirects"]:
        print(re["title"] + " redirect to " + v["title"])
