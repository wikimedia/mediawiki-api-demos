#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_pages_revisions.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get revision data with content for pages
    with titles [[API]] and [[Main Page]]

    MIT License
"""

import requests

S = requests.Session()

URL = "https://mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "API|Main Page",
    "rvprop": "timestamp|user|comment|content",
    "rvslots": "main",
    "formatversion": "2",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
