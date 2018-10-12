#!/usr/bin/python3

<<<<<<< HEAD
""" purge.py
    MediaWiki Action API Code Samples
    Demo of `purge` module: Sending post request to  purge first 10 pages in the main namespace
=======
"""
    purge.py
    
    MediaWiki Action API Code Samples
    Demo of `purge` module: Sending post request to purge first 10 pages in the main namespace
>>>>>>> Modified code samples for API:Purge
    MIT license
"""

import requests

<<<<<<< HEAD
URL = 'https://en.wikipedia.org/w/api.php'

PARAMS = {"action": "purge",
          "generator": "allpages",
          "gapnamespace": "0",
          "gaplimit": "10",
          "format": "json"
}

RESPONSE = requests.post(URL, data=PARAMS)

print(RESPONSE.text)
=======
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "purge",
    "generator": "allpages",
    "gapnamespace": "0",
    "gaplimit": "10",
    "format": "json"
}

R = requests.post(url=URL, data=PARAMS)
print(R.text)
>>>>>>> Modified code samples for API:Purge
