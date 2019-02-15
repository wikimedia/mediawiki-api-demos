#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    geoimagesearch.py

    MediaWiki Action API Code Samples
    Demo of `Geosearch` module: Use generator module
	to get search results for pages near Wikimedia HQ
	with images

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "ggscoord": "37.7891838|-122.4033522",
    "generator": "geosearch",
    "prop": "coordinates|pageimages"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['pages']

for k, v in PLACES.items():
    print(str(v['title']) + ": " + str(v['thumbnail']['source']))
