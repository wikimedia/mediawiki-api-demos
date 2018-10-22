#!/usr/bin/python3

"""
    get_max_revisions_w_content_and_backlinks.py
    MediaWiki Action API Code Samples
    Demo of `Lists` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'format':"json",
    'titles':"Winnipeg,_Manitoba",
    'prop':"revisions",
    'rvprop':"content",
    'rvlimit':"max",
    'list':"backlinks",
    'bltitle':"Winnipeg,_Manitoba",
    'bllimit':"max"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
