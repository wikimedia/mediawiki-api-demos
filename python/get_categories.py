#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_categories.py

    MediaWiki Action API Code Samples
    Demo of `Categories` module: Get categories associated with a page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "categories",
    "titles": "Janelle Monáe"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
