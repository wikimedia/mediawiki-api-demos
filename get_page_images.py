#!/usr/bin/python3

"""
    get_page_images.py

    MediaWiki Action API Code Samples
    Demo of `Images` module: Send a GET request to obtain a JSON
    object listing all of the image files embedded on a single
    page.

    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':'query',
    'format':'json',
    'prop':'images',
    'titles':'Albert Einstein'
}

R = S.get(url=URL, params=PARAMS)

DATA = R.json()
print(DATA)
