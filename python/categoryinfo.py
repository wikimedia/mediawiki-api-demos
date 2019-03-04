#!/usr/bin/python3

"""
    categoryinfo.py

    MediaWiki Action API Code Samples
    Demo of `...` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'format':"json",
    'titles':"Albert|Category:Foo|Category:Infobox",
    'prop':"categoryinfo",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)