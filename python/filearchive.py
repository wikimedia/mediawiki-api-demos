#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    filearchive.py

    MediaWiki API Demos
    Demo of `Filearchive` module: Enumerate 3 deleted files from filearchive table in descending order.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "falimit": "3",
    "list": "filearchive",
    "fadir": "descending",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
