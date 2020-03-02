#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    pageprops.py

    MediaWiki API Demos
    Demo of `Pageprops` module: Get various properties defined in the page content

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Albert Einstein",
    "prop": "pageprops",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
