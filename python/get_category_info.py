#!/usr/bin/python3

"""
    get_category_info.py

    MediaWiki Action API Code Samples
    Demo of `Categoryinfo` module: Get information about few categories
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Albert|Category:Foo|Category:Infobox",
    "prop": "categoryinfo"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
