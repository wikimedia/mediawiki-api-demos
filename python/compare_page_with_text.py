#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    compare_page_with_text.py

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare a revision of a page to some text
    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "compare",
    "format": "json",
    "fromrev": "829678781",
    "totext": "test%20edit,%20please%20ignore"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
