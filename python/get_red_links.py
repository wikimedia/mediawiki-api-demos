#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_red_links.py

    MediaWiki Action API Code Samples
    Demo of `Links` module: List first 20 missing links from all links on given page(s).

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "gpllimit": "20",
    "generator": "links",
    "format": "json",
    "prop": "links",
    "titles": "Wikipedia:Requested articles/Arts and entertainment",
    "action": "query"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGE_SET = DATA['query']['pages']
MISSING_PAGES_TITLES = []

for current_page in DATA['query']['pages']:
    MISSING_PAGES_TITLES.append(PAGE_SET[current_page]['title'])

print(MISSING_PAGES_TITLES)
