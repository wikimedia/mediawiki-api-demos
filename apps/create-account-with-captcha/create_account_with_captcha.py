#!/usr/bin/python3

"""
    create_account_with_captcha.py

    MediaWiki Action API Code Samples
    Demo of `createaccount` module: Create an account on a wiki with a special
    authentication extension installed. This example considers a case of a wiki
    where captcha is enabled through extensions like ConfirmEdit
    (https://www.mediawiki.org/wiki/Extension:ConfirmEdit)

    MIT license
"""

import requests
from flask import Flask, render_template, flash, request

S = requests.Session()
WIKI_URL = "https://test.wikipedia.org"
API_ENDPOINT = WIKI_URL + "/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = 'enter_your_secret_key'


@APP.route("/", methods=['GET', 'POST'])
def show_form():
    """ Render form template and handle form submission request """

    fields = get_form_fields()
    captcha = fields['CaptchaAuthenticationRequest']
    captcha_url = WIKI_URL + captcha['captchaInfo']['value']
    captcha_id = captcha['captchaId']['value']

    display_fields = []
    user_fields = []
    captcha_fields = []

    for field in fields:
        for name in fields[field]:
            details = {
                'name': name,
                'type': fields[field][name]['type'],
                'label': fields[field][name]['label']
            }

            if field != "CaptchaAuthenticationRequest":
                user_fields.append(details)
            else:
                if name == 'captchaWord':
                    captcha_fields.append(details)

    display_fields = user_fields + captcha_fields

    if request.method == 'POST':
        create_account(request.form, captcha_id)

    return render_template('create_account_form.html', \
        captcha=captcha_url, fields=display_fields)


def get_form_fields():
    """ Fetch the form fields from `authmanagerinfo` module """

    result = {}
    response = S.get(url=API_ENDPOINT, params={
        'action': 'query',
        'meta': 'authmanagerinfo',
        'amirequestsfor': 'create',
        'format': 'json'
    })
    data = response.json()

    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for field in fields:
        if field['id'] in ('MediaWiki\\Auth\\UserDataAuthenticationRequest', \
            'CaptchaAuthenticationRequest', 'MediaWiki\\Auth\\PasswordAuthenticationRequest'):
            result[field['id']] = field['fields']

    return result


def create_account(form, captcha_id):
    """ Send a post request along with create account token, user information
     and return URL to the API to create an account on a wiki """

    createtoken = fetch_create_token()
    response = S.post(url=API_ENDPOINT, data={
        'action': 'createaccount',
        'createtoken': createtoken,
        'username': form['username'],
        'password': form['password'],
        'retype': form['retype'],
        'email': form['email'],
        'createreturnurl': 'http://127.0.0.1:5000/',
        'captchaId': captcha_id,
        'captchaWord': form['captchaWord'],
        'format': 'json'
    })

    data = response.json()
    createaccount = data['createaccount']

    if createaccount['status'] == "PASS":
        flash('Success! An account with username ' + \
            form['username'] + ' has been created!')
    else:
        flash('Oops! Something went wrong -- ' + \
            createaccount['messagecode'] + "." + createaccount['message'])

def fetch_create_token():
    """ Fetch create account token via `tokens` module """

    response = S.get(url=API_ENDPOINT, params={
        'action': 'query',
        'meta': 'tokens',
        'type': 'createaccount',
        'format': 'json'
    })

    data = response.json()
    return data['query']['tokens']['createaccounttoken']


if __name__ == "__main__":
    APP.run()
