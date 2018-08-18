#!/usr/bin/python3

"""
    geocoordinates.py

    MediaWiki Action API Code Samples
    Demo of `Geosearch` module: Obtain coordinates for wiki pages nearby
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

TITLE = 'Wikimedia Foundation'

PARAMS = {
    'action':"query",
    'prop':"coordinates",
    'titles': TITLE,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']

for k, v in PAGES.items():
    print("Latitute: " + str(v['coordinates'][0]['lat']))
    print("Longitude: " + str(v['coordinates'][0]['lon']))
