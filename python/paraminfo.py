#This file is partly auto-generated

#!/usr/bin/python3

"""
    paraminfo.py

    MediaWiki Action API Code Samples
    Demo of `Paraminfo` module: Obtain information about other modules.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "paraminfo",
    "format": "json",
    "modules": "parse|query+info|query+blah"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
