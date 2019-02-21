#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_alllinks_red.py

    MediaWiki Action API Code Samples
    Demo of `Alllinks_red` module: List all the links 
    and check if the link is a red link or 
    not.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "format": "json",
    "action": "query",
    "generator":"links",
    "titles": "Title",
    "gpllimit": "max",
    "prop": "links"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
