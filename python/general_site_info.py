#!/usr/bin/python3

"""
    general_site_info.py

    MediaWiki API Demos
    Demo of `Siteinfo` module: Obtain general site info.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "siteinfo",
    "formatversion": "2",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
