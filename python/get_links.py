#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_links.py

    MediaWiki API Demos
    Demo of `Links` module: Get all links on the given page(s)

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Albert Einstein",
    "prop": "links"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k,v in PAGES.items():
    for l in v["links"]:
        print(l["title"])
