#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_allusers.py

    MediaWiki Action API Code Samples
    Demo of `Allusers` module: Get all users, starting from those whose name
    begins with the string, 'Drov'.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allusers",
    "auprefix": "Drov"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
