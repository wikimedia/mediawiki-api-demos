#!/usr/bin/python3

"""
    get_category_info.py

    MediaWiki API Demos
    Demo of `Categoryinfo` module: Get information about few categories
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Category:Foo|Category:Infobox templates",
    "prop": "categoryinfo"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k,v in PAGES.items():
    print(v["title"] + " has " + str(v["categoryinfo"]["pages"]) + " pages.")
