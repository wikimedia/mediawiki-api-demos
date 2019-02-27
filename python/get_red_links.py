#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_red_links.py

    MediaWiki Action API Code Samples
    Demo of `Links` module: List red links in a page.

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
pages = DATA['query']['pages']
missing_pages = {}

for page in pages:
	if int(page) < 0:
		missing_page = pages[page]
		missing_pages.update({page:missing_page})

print(missing_pages)