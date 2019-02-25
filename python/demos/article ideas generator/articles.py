#!/usr/bin/python3

"""
    articles.py

    MediaWiki Action API Code Samples

    Article ideas generator app: suggests articles from various categories
    that don't yet exist on English Wikipedia. The app uses action=parse module
    and prop=links module as a generator.

    MIT license
"""

from flask import Flask, request, render_template
import requests

APP = Flask(__name__)
SESSION = requests.Session()
API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'
PAGE = {}


@APP.route('/', methods=['GET', 'POST'])
def index():
    """ Displays the index page accessible at '/'
    """
    global PAGE
    results = []

    if request.method == 'POST':
        if 'category' in request.form:
            PAGE['name'] = PAGE['name'] + '/' + \
                request.form.to_dict()['category']
            PAGE['type'] = 'subcategory'
            results = get_page_sections(PAGE['name'])
        elif 'subcategory' in request.form:
            PAGE['name'] = PAGE['name'] + '#' + \
                request.form.to_dict()['subcategory']
            PAGE['type'] = 'links'
            results = get_red_links(PAGE['name'])
    else:
        PAGE = {'name': 'Wikipedia:Requested_articles', 'type': 'category'}
        results = get_page_sections(PAGE['name'])

    return render_template(
        "articles.html",
        results=results,
        pagetype=PAGE['type'])


def get_page_sections(page):
    """ Get page sections
    """
    params = {
        "action": "parse",
        "page": page,
        "prop": "sections",
        "format": "json"
    }

    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()
    parsed_sections = data and data['parse'] and data['parse']['sections']
    sections = []

    for section in parsed_sections:
        if section['toclevel'] == 1:
            sections.append(section['line'])

    return sections


def get_red_links(title):
    """ Get missing links on a page
    """
    params = {
        "action": "query",
        "titles": title,
        "generator": "links",
        "gpllimit": 20,
        "format": "json"
    }

    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()
    pages = data and data['query'] and data['query']['pages']
    links = []

    for page in pages.itervalues():
        links.append(page['title'])

    return links


if __name__ == '__main__':
    APP.run()
