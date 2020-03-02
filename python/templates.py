#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    templates.py

    MediaWiki API Demos
    Demo of `Templates` module: Get a list of templates used on a page

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Albert Einstein",
    "prop": "templates",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
