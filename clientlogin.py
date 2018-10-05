#!/usr/bin/python3

"""
    clientlogin.py

    MediaWiki Action API Code Samples
    Demo of `clientlogin` module: Sending post request to login
    MIT license
    Flask web form tutorial code borrowed from https://pythonspot.com/flask-web-forms/
"""

import requests
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class MWLoginForm(Form):
    """ Design MediaWiki Login form using Flask's Form class
    """
    name = TextField('Name:')
    password = TextField('Password:')

@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Render form template and handle form submission request
    """
    form = MWLoginForm(request.form)

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        start_client_login(name, password)

    return render_template('clientlogin_form.html', form=form)

def start_client_login(name, password):
    """ Fetch login token and send a request to client login
    """
    login_token = fetch_login_token()

    resp = S.post(url=URL, data={
        'action': "clientlogin",
        'username': name,
        'password': password,
        'loginreturnurl': 'enter_a_url',
        'logintoken': login_token,
        'format': "json"
    })

    data = resp.json()

    if data['clientlogin']['status'] == 'PASS':
        flash('Login success! Welcome, ' + data['clientlogin']['username'] + '!')
    else:
        flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])

def fetch_login_token():
    """ Fetch login token
    """
    resp = S.get(
        url=URL,
        params={
            'action': "query",
            'meta': "tokens",
            'type': "login",
            'format': "json"})
    data = resp.json()
    return data['query']['tokens']['logintoken']

if __name__ == "__main__":
    APP.run()
