#!/usr/bin/python3

"""
    get_deleted_revisions.py

    MediaWiki Action API Code Samples
    Demo of `...` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'drstart':"20070904235959",
    'drend':"20070904000000",
    'list':"deletedrevs",
    'drprop':"revid|user|minor|len|token",
    'drlimit':"6",
    'druser': "Catrope",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)