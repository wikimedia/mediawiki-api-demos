#!/usr/bin/python3

"""
    get_recent_category_items.py

    MediaWiki Action API Code Samples
    Demo of `Categorymembers` module : Get the ten articles most recently added to a category.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Category:Physics",
    'cmsort': "timestamp",
    'cmdir': "desc",
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
