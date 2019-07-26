#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_querypage_list.py

    MediaWiki API Demos
    Demo of `Querypage` module: List first 10 pages which are uncategorized

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "qplimit": "10",
    "action": "query",
    "qppage": "Uncategorizedpages",
    "list": "querypage",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

QUERYPAGE = DATA['query']['querypage']['results']

for p in QUERYPAGE:
    print(str(p['title']))
