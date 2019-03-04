#!/usr/bin/python3

"""
    create_account_with_captcha.py

    MediaWiki Action API Code Samples
    Demo of `createaccount` module: Create an account on a wiki with a special
    authentication extension installed. This example considers a case of a wiki
    where captcha is enabled through extensions like ConfirmEdit
    (https://www.mediawiki.org/wiki/Extension:ConfirmEdit)

    This demo app uses Flask (a Python web development framework).

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
    """ Render form template and handle form submission request
    """

    captcha_fields = get_captcha_fields()
    captcha_url = WIKI_URL + captcha_fields['captchaInfo']['value']

    if request.method == 'POST':
        details = {
            'name': request.form['username'],
            'password': request.form['password'],
            'confirm_password': request.form['confirm-password'],
            'email': request.form['email'],
            'captcha_word': request.form['captcha-word'],
            'captcha_id': captcha_fields['captchaId']['value']
        }

        create_account(details)

    return render_template(
        'create_account_form.html',
        captcha=captcha_url
        )


def get_captcha_fields():
    """ Fetch the captcha fields from `authmanagerinfo` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json'})

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == 'CaptchaAuthenticationRequest':
            return k and k['fields']
    return None

def get_password_fields():
    """ Fetch the MediaWiki\\Auth\\Password fields from `authmanagerinfo` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json'})

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == '':
            return k and k['fields']
    return None


def get_campaigns_fields():
    """ Fetch the Campaigns fields from `authmanagerinfo` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json'})

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == 'CampaignsAuthenticationRequest':
            return k and k['fields']
    return None


def get_username_fields():
    """ Fetch the MediaWiki\\Auth\\Username fields from `authmanagerinfo` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json'})

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == 'MediaWiki\\Auth\\UsernameAuthenticationRequest':
            return k and k['fields']
    return None


def get_userdata_fields():
    """ Fetch the MediaWiki\\Auth\\UserData fields from `authmanagerinfo` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'authmanagerinfo',
            'amirequestsfor': 'create',
            'format': 'json'})

    data = response.json()
    query = data and data['query']
    authmanagerinfo = query and query['authmanagerinfo']
    fields = authmanagerinfo and authmanagerinfo['requests']

    for k in fields:
        if k['account'] == 'MediaWiki\\Auth\\UserDataAuthenticationRequest':
            return k and k['fields']
    return None




"""edited part"""

def create_account(details):
    """ Send a post request along with create account token, user information
    and return URL to the API to create an account on a wiki """

    createtoken = fetch_create_token()

    response = S.post(url=API_ENDPOINT, data={
        'action': 'createaccount',
        'createtoken': createtoken,
        'username': details['name'],
        'password': details['password'],
        'retype': details['confirm_password'],
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
            'Success! An account with username ' + details['name'] + ' has been created!')
    else:
        flash(
            'Oops! Something went wrong -- ' + createaccount['messagecode'] + "." +
            createaccount['message'])


def fetch_create_token():
    """ Fetch create account token via `tokens` module """

    response = S.get(
        url=API_ENDPOINT,
        params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'createaccount',
            'format': 'json', })

    data = response.json()
    return data['query']['tokens']['createaccounttoken']


if __name__ == "__main__":
    APP.run()
