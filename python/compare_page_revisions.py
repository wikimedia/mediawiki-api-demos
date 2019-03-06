#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    compare_page_revisions.py

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare two revisions from the same page
    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "compare",
    "format": "json",
    "fromrev": "139992",
    "torev": "139993"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
