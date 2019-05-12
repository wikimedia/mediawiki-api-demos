#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    languagesearch.py

    MediaWiki API Demos
    Demo of `Languagesearch` module: Search for a language in any language

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "languagesearch",
    "search": "Gu", #Could be name of the language, its iso code or native name
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['languagesearch'])
