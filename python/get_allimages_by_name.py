#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_allimages_by_name.py

    MediaWiki Action API Code Samples
    List all images in the namespace, starting from files that begin with 'I'. Limit the initial response to just the first three images. 

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allimages",
    "aifrom": "I",
    "ailimit": "3"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
