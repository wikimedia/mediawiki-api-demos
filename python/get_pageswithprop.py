#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_pageswithprop.py

    MediaWiki API Demos
    Demo of `Pageswithprop` module:List all pages using a given page property..

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "list": "pageswithprop",
    "pwppropname": "displaytitle",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGESWITHPROP = DATA["query"]["pageswithprop"]

for p in PAGESWITHPROP:
    print(p["title"])
