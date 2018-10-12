#!/usr/bin/python3

""" purge_twopages.py
    MediaWiki Action API Code Samples
    Demo of `purge` module: Sending post request to purge cache of two pages
    MIT license
"""

import requests

URL = 'https://en.wikipedia.org/w/api.php'

PARAMS = {"action": "purge",
          "titles": "Main_Page|Nonexistent",
          "format": "json"
}  

RESPONSE = requests.post(URL, data=PARAMS)

print(RESPONSE.text)
