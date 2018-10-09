#!/usr/bin/python3
""" purge.py
    MediaWiki Action API Code Samples
    Demo of `purge` module: Sending post request to purge cache of one page
    MIT license
"""
import requests
URL = 'https://en.wikipedia.org/w/api.php'
PARAMS = {"action": "purge",
          "generator": "allpages",
          "gapnamespace": "0",
          "gaplimit": "10",
          "format": "json"}
RESPONSE = requests.post(URL, data=PARAMS)
print(RESPONSE.text)
