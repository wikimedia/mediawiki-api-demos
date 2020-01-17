#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    iwbacklinks.py

    MediaWiki API Demos
    Demo of `Iwbacklinks` module: Get pages linking to wikibooks:Main_Page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "list": "iwbacklinks",
    "iwblprefix": "wikibooks",
    "iwbltitle": "Main_Page",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
