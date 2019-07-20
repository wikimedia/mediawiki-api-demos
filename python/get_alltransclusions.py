#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_alltransclusions.py

    MediaWiki API Demos
    Demo of `Alltransclusions` module: Get three unique pages in the main
    namespace which contain transclusions.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "alltransclusions",
    "atunique": "1",
    "atnamespace": "0",
    "atlimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

TRANSCLUSIONS = DATA["query"]["alltransclusions"]

for t in TRANSCLUSIONS:
    print(t["title"])
