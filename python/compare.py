#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    compare.py

    MediaWiki API Demos
    Demo of `Compare` module: Compare the current revisions of two different pages.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "compare",
    "fromtitle": "Template:Unsigned",
    "totitle": "Template:UnsignedIP",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
