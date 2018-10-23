#!/usr/bin/python3
""" get_pages.py
    MediaWiki Action API Code Samples
    Sending GET request to obtain a JSON object listing pages of 3 categories
    MIT license
"""
import requests

S = requests.Session()
URL = 'https://en.wikipedia.org/w/api.php'
PARAMS = {"action": "query",
          "list": "allpages",
          "apfrom": "Ab",
          "aplimit": "3",
          "apnamespace":"14",
          'format':"json"
          }
R = S.get(url=URL, params=PARAMS)
DATA=R.json()
print(DATA)