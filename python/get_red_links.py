#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_red_links.py

    MediaWiki Action API Code Samples
    Demo of `Links` module: Use generator module
    to get all links on the given page(s)
    and identify if the link is a red link or not

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "links",
    "titles": "Title",
    "generator": "links"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
