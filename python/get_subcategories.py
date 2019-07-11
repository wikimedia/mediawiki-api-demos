#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_subcategories.py

    MediaWiki API Demos
    Demo of `Categorymembers` module : Get ten subcategories of a category

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "cmtitle": "Category:Wikipedia",
    "cmtype": "subcat",
    "list": "categorymembers",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["categorymembers"]

for page in PAGES:
    print( page["title"] )
