#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_links.py

    MediaWiki Action API Code Samples
    Demo of `Links` module: Get all links on the given page(s)

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Albert Einstein",
    "prop": "links"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
