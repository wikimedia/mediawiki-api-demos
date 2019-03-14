#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_langlinks.py

    MediaWiki Action API Code Samples
    Demo of `Langlinks` module: Demo to gets a list of first 20 language links from the provided pages to other languages.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

#list of first 20 language links with the localised language name.

PARAMS = {
    "llprop" : "langname",
    "format" : "json",
    "lllimit": "20",
    "prop"   : "langlinks",
    "titles" : "Main Page",
    "action" : "query"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
