#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    linkshere.py

    MediaWiki API Demos
    Demo of `Linkshere` module: Get a list of pages linking to a given page

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Main Page",
    "prop": "linkshere",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
