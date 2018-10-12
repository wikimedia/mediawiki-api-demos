#!/usr/bin/python3

"""
    purge_two_pages.py

    MediaWiki Action API Code Samples
    Demo of `purge` module: Sending post request to purge Sending post request to purge two or more pages
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "purge",
    "titles": "Main_Page|Nonexistent",
    "format": "json"
}

R = requests.post(url=URL, data=PARAMS)
print(R.text)