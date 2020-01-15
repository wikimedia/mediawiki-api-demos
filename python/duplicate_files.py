#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    duplicate_files.py

    MediaWiki API Demos
    Demo of `Duplicatefiles` module: List duplicates of the given files.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Image:1995.jpg|Image:Welcome.gif",
    "prop": "duplicatefiles",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
