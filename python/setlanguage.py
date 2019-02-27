#!/usr/bin/python3

"""
    setlanguage.py

    MediaWiki Action API Code Samples
    Demo of `SetPageLanguage` module: POST request to change the language of a page

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "setpagelanguage",
    "lang": "default",
    "token": "+\\",
    "title": "Help:Starting_a_new_page",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
