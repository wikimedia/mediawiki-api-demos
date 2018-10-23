#!/usr/bin/python3
""" get_pages.py
    MediaWiki Action API Code Samples
    Sending GET request to obtain a JSON object listing all 5pages gotten, starting from "kre"
    MIT license
"""
import requests

S = requests.Session()
URL = 'https://en.wikipedia.org/w/api.php'
PARAMS = {"action": "query",
          "list": "allpages",
          "apfrom": "kre",
          "aplimit": "5",
          'format':"json"
          }
R = S.get(url=URL, params=PARAMS)
DATA=R.json()

print(DATA)