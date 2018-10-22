#!/usr/bin/python3

"""
    get_25_category_pages.py
    MediaWiki Action API Code Samples
    Demo of `Lists` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'format':"json",
    'list': "categorymembers",
    'cmtitle': "Category:Physics",
    'cmlimit': 25
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
