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
    "format": "json",
    "pageid": "123",
    "lang": "eu",
    "token": "e17ac3bb8d7dd0c4f5e4fd1f84cd21095c76c2cc+\\"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
