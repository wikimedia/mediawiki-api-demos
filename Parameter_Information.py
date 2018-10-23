#!/usr/bin/python3
""" Parameter_Information.py
    MediaWiki Action API Code Samples
    Sending GET request: Getting information about 
    'action'='parse', 'prop'='info' query submodule, 
    and a bogus query module
    MIT license
"""
import requests

S = requests.Session()
URL = 'https://en.wikipedia.org/w/api.php'
PARAMS = {"action": "paraminfo",
          "modules": "parse|query+info|query+blah",
          
          'format':"json"
          }
R = S.get(url=URL, params=PARAMS)
DATA=R.json()
print(DATA)