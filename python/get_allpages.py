#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allpages.py

    MediaWiki API Demos
    Demo of `Allpages` module: Get all pages whose title contains the text "Jungle," in whole or part.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "apfrom": "jungle",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
