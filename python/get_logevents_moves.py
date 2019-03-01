#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_logevents_moves.py

    MediaWiki Action API Code Samples
    Demo of `Logevents` module: List the 3 most recent page moves.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "letype": "move",
    "list": "logevents",
    "lelimit": "3",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
