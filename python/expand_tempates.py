#!/usr/bin/python3

"""
    expand_templates.py

    MediaWiki API Demos
    Demo of `Expandtemplates` module: Expand the Project:Sandbox template.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "expandtemplates",
    "text": "{{Project:Sandbox}}",
    "prop": "wikitext",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
