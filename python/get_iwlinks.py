#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    python/get_iwlinks.py

    MediaWiki API Demos
    Demo of `Iwlinks` module: Get the interwiki links from a given page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "iwlinks",
    "titles": "Albert Einstein"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
