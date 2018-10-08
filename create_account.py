#!/usr/bin/python3

"""
    create_account.py

    MediaWiki Action API Code Samples
    Demo of `Createaccount` module: Create an account on a Wiki
    MIT license
"""

import requests
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators

S = requests.Session()
WIKI_URL = "https://test.wikipedia.org"
API_ENDPOINT = WIKI_URL + "/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = 'enter_your_secret_key'

CAPTCHA_FIELDS = {}


@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Render form template and handle form submission request
    """

    form = MWCreateAccountForm(request.form)
    captcha_url = WIKI_URL + CAPTCHA_FIELDS['captchaInfo']['value']

    if request.method == 'POST':
        details = {
            'name': request.form['name'],
            'password': request.form['password'],
            'retype': request.form['retype'],
            'email': request.form['email'],
            'captcha_word': request.form['captchaWord'],
            'captcha_id': CAPTCHA_FIELDS['captchaId']['value']
        }

        create_account(details)

    return render_template(
        'create_account_form.html',
        form=form,
        captcha=captcha_url)


def create_account(details):
    """ Fetch create account token"""

    createtoken = fetch_create_token()

    response = S.post(url=API_ENDPOINT, data={
        'action': 'createaccount',
        'createtoken': createtoken,
        'username': details['name'],
        'password': details['password'],
        'retype': details['retype'],
        'email': details['email'],
        'createreturnurl': 'http://127.0.0.1:5000/',
        'captchaId': details['captcha_id'],
        'captchaWord': details['captcha_word'],
        'format': 'json',
    })

    data = response.json()
    createaccount = data['createaccount']

    if createaccount['status'] == "PASS":
        flash(
            'Success! An account with username ' +
            details['name'] +
            ' has been created!')
    else:
        flash(
            'Oops! Something went wrong -- ' +
            createaccount['messagecode'] +
            "." +
            createaccount['message'])


def fetch_create_token():
    """ Fetch create account token"""

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'createaccount',
            'format': 'json', })

    data = response.json()
    return data['query']['tokens']['createaccounttoken']


def get_captcha_fields():
    """ Get captcha fields """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json', })

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == 'CaptchaAuthenticationRequest':
            return k and k['fields']
    return None


class MWCreateAccountForm(Form):
    """ Design MediaWiki Create Account form using Flask's Form class
    """

    name = TextField(
        'Username', validators=[validators.required()],
        render_kw={"placeholder": "Enter your username"})
    password = TextField(
        'Password', validators=[validators.required()],
        render_kw={"placeholder": "Enter a password"})
    retype = TextField(
        'Confirm password', validators=[validators.required()],
        render_kw={"placeholder": "Enter password again"})
    email = TextField(
        'Email address (optional)', validators=[validators.required()],
        render_kw={"placeholder": "Enter your email address"})
    captchaWord = TextField(
        'Captcha security check', validators=[validators.required()],
        render_kw={"placeholder": "Enter the text you see on the image below"})


if __name__ == "__main__":
    CAPTCHA_FIELDS = get_captcha_fields()
    APP.run()
