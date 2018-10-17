#!/usr/bin/python3

"""
    images.py

    MediaWiki Action API Code Samples
    Demo of `Images` module: Sending GET request to images
    MIT license
"""
# Note: This code relies on the third party library, requests. 
# Be sure to install it via your favorite package manager!
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Send a GET request to the images endpoint.

PARAMS = {
  'action':'query',
  'format':'json',
  'prop':'images',
  'titles':'Albert Einstein'
}

R = S.get(url=URL, params=PARAMS)

DATA = R.json()
print(DATA)
