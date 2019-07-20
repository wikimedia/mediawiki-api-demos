#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_imageusage.py

    MediaWiki API Demos
    Demo of `Imageusage` module: List the first 3 pages that use a given image title

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "imageusage",
    "iutitle": "File:Wiki_logo_Nupedia.jpg",
    "iulimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["imageusage"]

for p in PAGES:
    print(p["title"])
