#!/usr/bin/python3

"""
    compare.py

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare the current revisions of two different pages
    
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"compare",
    'format':"json",
    'fromtitle':'Template:Unsigned',
    'totitle':'Template:UnsignedIP'
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
