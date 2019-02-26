#!/usr/bin/python3

"""
    get_allpages.py

    MediaWiki Action API Code Samples
    Demo of `Allpages` module: Get all pages whose title contains
    the text "Jungle," in whole or part.

    MIT License
"""
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"	

PARAMS = {
    "action": "query",
    "format": "json",
    "action": "compare",
   	"fromtitle":"Jungle",
   	"totitle":"JunglePup",
   	"prop":"ids|user|title"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
