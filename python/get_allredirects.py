#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_allredirects.py

    MediaWiki API Demos
    Demo of `Allredirects` module: Get the first three unique pages containing
    redirects to the main namespace.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allredirects",
    "arunique": "1",
    "arnamespace": "0",
    "arlimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
