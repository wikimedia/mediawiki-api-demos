#This file is partly auto-generated

#!/usr/bin/python3

"""
    logout.py

    MediaWiki Action API Code Samples
    Demo of `Logout` module: Log out and clear session data.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "logout",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
