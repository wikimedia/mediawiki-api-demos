#This file is partly auto-generated

#!/usr/bin/python3

"""
    geosearch.py

    MediaWiki Action API Code Samples
    Demo of `Geosearch` module: Search for wiki pages nearby

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "format": "json",
    "list": "geosearch",
    "gscoord": "37.7891838|-122.4033522",
    "gslimit": "10",
    "gsradius": "10000",
    "action": "query"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['geosearch']

for place in PLACES:
    print(place['title'])
