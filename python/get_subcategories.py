#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_subcategories.py

    MediaWiki Action API Code Samples
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

print(DATA)
