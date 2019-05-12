#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_allimages_by_name.py

    MediaWiki API Demos
    List all images in the namespace, starting from files that begin with
    'Graffiti_000'. Limit the initial response to just the first three images.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allimages",
    "aifrom": "Graffiti_000",
    "ailimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
