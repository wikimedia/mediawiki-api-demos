#!/usr/bin/python3

"""
    MediaWiki Action API Code Samples
    Demo of `Categorymembers` module : List 20 items in a category.
    MIT license
    """

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Category:Physics",
    'cmlimit': 20,
    'format': "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
