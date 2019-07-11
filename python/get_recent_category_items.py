#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_recent_category_items.py

    MediaWiki API Demos
    Demo of `Categorymembers` module : Get the ten articles most recently added to a category

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "cmdir": "desc",
    "format": "json",
    "list": "categorymembers",
    "action": "query",
    "cmtitle": "Category:Physics",
    "cmsort": "timestamp"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["categorymembers"]

for page in PAGES:
    print(page["title"])
