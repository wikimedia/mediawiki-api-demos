#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    opensearch.py

    MediaWiki Action API Code Samples
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "OpenSearch",
    "namespace": "0",
    "search": "Hampi",
    "limit": "5",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
