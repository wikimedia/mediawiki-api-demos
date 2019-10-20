#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    rsd.py

    MediaWiki API Demos
    Demo of `Rsd` module: Get request to export an RSD schema.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "rsd",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
