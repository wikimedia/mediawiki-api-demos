#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_embedded_lists.py
    MediaWiki Action API Code Samples
    Demo of `Embeddedin` module: Get all page(s) that
    embed the given title.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "embeddedin",
    "eititle": "Computer",
    "eilimit": "20"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
