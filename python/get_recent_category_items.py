#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_recent_category_items.py

    MediaWiki Action API Code Samples
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

print(DATA)
