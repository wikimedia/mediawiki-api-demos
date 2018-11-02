#!/usr/bin/python3

"""
    searchdemo.py

    MediaWiki Action API Code Samples
    Demo of `API:Search`: Search for a text or title

    Articles in the 'articles.json' file are pulled 
    from the link below:
    https://en.wikipedia.org/wiki/Wikipedia:Requested_articles/Biography/By_profession 
    
    MIT license
"""

import json
import requests
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import SelectField

# app config
DEBUG = True
APP = Flask(__name__)
APP.config['SECRET_KEY'] = '6758'
Bootstrap(APP)

SESSION = requests.Session()

# Wikipedia API details
URL = "https://en.wikipedia.org/w/api.php"

@APP.before_first_request
def load_data_from_json_file():
    """ Load categories and articles from json file
    """
    with open('articles.json') as file:
        data = json.load(file)
    return data

ARTICLES_DATA = load_data_from_json_file()

def get_category_names():
    """ Get category names
    """
    c_names = []
    for c_item in range(0, len(ARTICLES_DATA['categories'])):
        c_names.append(ARTICLES_DATA['categories'][c_item]['name'])
    return c_names

def get_articles_for_a_category(category):
    """ Get articles for a category
    """
    articles = []
    for c_item in range(0, len(ARTICLES_DATA['categories'])):
        if category == ARTICLES_DATA['categories'][c_item]['name']:
            articles = ARTICLES_DATA['categories'][c_item]['articles']
    return articles

def does_article_exists(title):
    """ Check if an articles with a title exists on English Wikipedia
    """
    params = {
        'action': "query",
        'list': "search",
        'srsearch': title,
        'format': "json"
    }

    res = SESSION.get(url=URL, params=params)
    data = res.json()
    query_res = data['query']['search']

    if query_res and query_res[0] and query_res[0]['title'] == title:
        return True

    return False

class CategoriesForm(FlaskForm):
    """ Build the suggest categories form with a select field
    """
    categories = get_category_names()
    category = SelectField(
        "Choose a category:", choices=[
            (c_item, c_item) for c_item in categories])

@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Display form
    """
    form = CategoriesForm()
    articles = None
    re_articles = []

    if request.method == "POST":
        name = request.form['category']
        articles = get_articles_for_a_category(name)

        for article in enumerate(articles):
            item = {}
            title = article[1]['title']
            item['title'] = title
            if does_article_exists(title):
                item['isThereAWikiPage'] = "Yes"
            else:
                item['isThereAWikiPage'] = "No"
            re_articles.append(item)

    return render_template(
        'search_form.html',
        form=form,
        re_articles=re_articles)


if __name__ == '__main__':
    APP.run()
