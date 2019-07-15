#!/usr/bin/python3

"""
    site_info.py

    MediaWiki Action API Code Samples
    Demo of `SiteInfo` module: GET request to return general site information

    MIT License
"""

import requests

S = requests.Session()

URL =  "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta":"siteinfo",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['query']['general'])