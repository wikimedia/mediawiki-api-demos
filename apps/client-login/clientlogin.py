#!/usr/bin/python3

"""
    clientlogin.py

    MediaWiki API Demos
    Demo of `clientlogin` module: Sending post request to login

    This demo app uses Flask (a Python web development framework).

    MIT license
"""

import requests
from flask import Flask, render_template, flash, request

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = 'enter_your_secret_key'


@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Render form template and handle form submission request """

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        start_client_login(username, password)

    return render_template('clientlogin_form.html')

def start_client_login(username, password):
    """ Send a post request along with login token, user information
    and return URL to the API to log in on a wiki """

    login_token = fetch_login_token()

    response = S.post(url=URL, data={
        'action': "clientlogin",
        'username': username,
        'password': password,
        'loginreturnurl': 'http://127.0.0.1:5000/',
        'logintoken': login_token,
        'format': "json"
    })

    data = response.json()

    if data['clientlogin']['status'] == 'PASS':
        flash('Login success! Welcome, ' + data['clientlogin']['username'] + '!')
    else:
        flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])

def fetch_login_token():
    """ Fetch login token via `tokens` module """

    response = S.get(
        url=URL,
        params={
            'action': "query",
            'meta': "tokens",
            'type': "login",
            'format': "json"})
    data = response.json()
    return data['query']['tokens']['logintoken']

if __name__ == "__main__":
    APP.run()
