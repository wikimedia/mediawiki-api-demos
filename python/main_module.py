#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    main_module.py

    MediaWiki API Demos
    Demo of `Main module` module: Get help for the main module.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "help",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.content

print(DATA)
