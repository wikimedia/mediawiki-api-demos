#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_red_links.py

    MediaWiki API Demos
    Demo of `Links` module to identify red or missing links on a page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "titles": "Wikipedia:Most-wanted_articles",
    "gpllimit": "20",
    "format": "json",
    "generator": "links"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
LINKS = []

for page in PAGES.values():
    if 'missing' in page:
        LINKS.append(page['title'])

print(LINKS)
