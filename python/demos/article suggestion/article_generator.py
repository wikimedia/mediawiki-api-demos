#!/usr/bin/python3

"""
    article_generator.py

    MediaWiki Action API Code Samples

    TODO: Article ideas generator app: places viewer app: Demo of ...

    Articles generated from:
    https://en.wikipedia.org/wiki/Wikipedia:Requested_articles
    
    MIT license
"""

from flask import Flask, request, render_template, jsonify
import requests

SESSION = requests.Session()
API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'

PARAMS = {
    "action": "parse",
    "page": "Wikipedia:Requested_articles",
    "prop": "wikitext",
    "section": 1,
    "format": "json"
}

res = SESSION.get(url=API_ENDPOINT, params=PARAMS)
data = res.json()

wikitext = data['parse']['wikitext']['*']
print(wikitext)
lines = wikitext.split('*')
entries = []

print(len(lines))

for line in lines: 
    #print(line)
    line = line.strip()
    print(line)
    if line.startswith("|"):
        table = line[2:].split('||')
        print(table)
        entry = table[0].split("|")[0].strip("'''[[]]\n"), table[0].split("|")[1].strip("\n")
        print(entry)
        entries.append(entry)

print(entries)


# APP = Flask(__name__)
# SESSION = requests.Session()
# API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'


# @APP.route('/', methods=['GET', 'POST'])
# def index():
#     """ Displays the index page accessible at '/'
#     """
#     PARAMS = {
#         "action": "parse",
#         "page": "Wikipedia:Requested_articles",
#         "prop": "wikitext",
#         "section": 1,
#         "format": "json"
#     }

#     res = SESSION.get(url=API_ENDPOINT, params=PARAMS)
#     data = res.json()

#     wikitext = data['parse']['wikitext']['*']
#     lines = wikitext.split('|-')
#     #print(lines)
#     entries = []

#     for line in lines:
#         #print(line)
#         line = line.strip()
#         if line.startswith("|"):
#             table = line[2:].split('||')
#             entry = table[0].split("|")[0].strip("'''[[]]\n"), table[0].split("|")[1].strip("\n")
#             entries.append(entry)

#     print(entries)

#     return render_template('articles.html', results=entries)


# if __name__ == '__main__':
#     APP.run()
