#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_redirects.py

    MediaWiki Action API Code Samples
    Demo of `Redirects` module: Get all redirects to the given page(s)

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Jacques Kallis",
    "prop": "redirects"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
