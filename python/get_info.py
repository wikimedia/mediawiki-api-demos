#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_info.py

    MediaWiki API Demos
    Demo of `Info` module: Send a GET request to display information about a page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Albert Einstein",
    "prop": "info",
    "inprop": "url|talkid"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
