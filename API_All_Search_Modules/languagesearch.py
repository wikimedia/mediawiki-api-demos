#!/usr/bin/python3

"""
    languagesearch.py

    MediaWiki Action API Code Samples
    Demo of `Languagesearch` module: Search for a language in any language
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

LANG_NAME = "Gu" #Could be name of the language, its iso code or native name

PARAMS = {
    'action':"languagesearch",
    'search':LANG_NAME,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['languagesearch'])
