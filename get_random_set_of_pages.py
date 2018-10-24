#!/usr/bin/python3

"""
    get_random_set_of_pages.py

    MediaWiki Action API Code Samples
    Demo of `Random` module: get random set of pages including information such as titles, content, images, etc.
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "revisions|images",
    "generator": "random"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.text

print(DATA)
