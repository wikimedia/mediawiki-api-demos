#!/usr/bin/python3

"""
    purge_two_pages.py

    MediaWiki API Demos
    Demo of `purge` module: Sending post request to purge two or more pages
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

R = S.post(url=URL, params=PARAMS)
DATA = R.text

print(DATA)
