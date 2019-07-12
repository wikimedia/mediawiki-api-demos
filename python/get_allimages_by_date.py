#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allimages_by_date.py

    MediaWiki API Demos
    List all images in the namespace, starting from January 1, 2010,
    at 18:05:46 UTC.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allimages",
    "aisort": "timestamp",
    "aistart": "2010-01-01T18:05:46Z"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

IMAGES = DATA["query"]["allimages"]

for img in IMAGES:
    print(img["title"])
