#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_protectedtitles.py

    MediaWiki API Demos
    Demo of `Protectedtitles` module: Get the first 2 titles which only sysops can create

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "protectedtitles",
    "ptlevel": "sysop",
    "ptlimit": "2"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
