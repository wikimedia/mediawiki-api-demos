#!/usr/bin/python3

"""
    purge_namespace_pages.py

    MediaWiki API Demos
    Demo of `purge` module: Sending post request to purge first 10 pages in the main namespace
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "purge",
    "generator": "allpages",
    "gapnamespace": "0",
    "gaplimit": "10",
    "format": "json"
}

R = S.post(url=URL, params=PARAMS)
DATA = R.text

print(DATA)
