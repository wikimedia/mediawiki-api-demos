#!/usr/bin/python3

"""
    login.py

    MediaWiki Action API Code Samples
    Demo of `Createaccount` module: Create an account on a Wiki
    MIT license
"""

import requests
from flask import Flask, render_template, request
from wtforms import Form, TextField, validators

S = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class MWCreateAccountForm(Form):
    """ Design MediaWiki Create Account form using Flask's Form class
   """
    name = TextField('name:', validators=[validators.required()])
    password = TextField(
        'Password:',
        validators=[
            validators.required(),
            validators.Length(
                min=3,
                max=35)])
    retype = TextField(
        'password:',
        validators=[
            validators.required(),
            validators.Length(
                min=3,
                max=35)])
    email = TextField(
        'Email:',
        validators=[
            validators.required(),
            validators.Length(
                min=6,
                max=35)])


@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Render form template and handle form submission request
   """
    form = MWCreateAccountForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        retype = request.form['password']
        email = request.form['email']
        start_create_account(name, password, retype, email)
    return render_template('create_my_account_form.html', form=form)


def start_create_account(name, password, retype, email):
    """ Fetch create account token"""

    create_account_token = fetch_create_account_token()
    response = S.post(url=URL, data={
        'action': 'createaccount',
        'createtoken': create_account_token,
        'username': name,
        'password': password,
        'retype': retype,
        'email': email,
        'createreturnurl': 'http://example.com/',
        'format': 'json',
    })
    data = response.json()
    print(data)

def fetch_create_account_token():
    """ Fetch create account token"""
    response = S.get(
        url=URL,
        params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'createaccount',
            'format': 'json', })
    data = response.json()
    return data['query']['tokens']['createaccounttoken']

def captcha_authentication():
    """Fetch captcha to help authenticate account creation
    """
    response = S.get(
        url=URL,
        params={
            "query": "cancreateaccounts",
            "id": "captchaAuthenticationRequest",
            "metadata": "type",
            "provider": "CaptchaAuthenticationRequest",
            "fields": "captchaId",
            "required": "required",
            "account": "CaptchaAuthenticationRequest"})
    data = response.json()
    return data['query']['id']['metadata']

if __name__ == "__main__":
    APP.run()
