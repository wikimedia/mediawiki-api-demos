#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import urllib
import os

from flask import Flask, render_template, request, Markup, \
    send_from_directory, session
from flask_mwoauth import MWOAuth
import requests_oauthlib
import requests
import qrcode
import qrcode.image.svg
import yaml


APP = Flask(__name__)
APP.secret_key = os.urandom(24)

# Load configuration from YAML file
__dir__ = os.path.dirname(__file__)
APP.config.update(yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))

# Get variables
BASE_URL = APP.config['OAUTH_MWURI']
API_ENDPOINT = BASE_URL + '/api.php'
CONSUMER_KEY = APP.config['CONSUMER_KEY']
CONSUMER_SECRET = APP.config['CONSUMER_SECRET']

# Register blueprint to app
MWOAUTH = MWOAuth(base_url=BASE_URL, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
APP.register_blueprint(MWOAUTH.bp)


# /index route for return_to
@APP.route('/index', methods=['GET'])
@APP.route('/', methods=['GET'])
def index():
    # Get the URL from the query string
    url = request.args.get('urltextBox')
    username = MWOAUTH.get_current_user(True)

    if url is None:
        return render_template('index.html', username=username)

    # Escape the unicode encoding from URL
    url = urllib.parse.unquote(url)

    # Get the file name based on current time
    current_time = str(datetime.datetime.now())
    get_filename = current_time.replace(':', '_').replace(' ', '_') + '.svg'
    file_withpath = 'static/qrcodes/' + get_filename

    # Create the QR Code File
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage, version=8)
    img.save(file_withpath)

    # Read the QR Code File
    svg = open(file_withpath).read()

    return render_template('index.html', url=url, fileName=get_filename,
                           username=username, src=Markup(svg))


@APP.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(directory='static/qrcodes', filename=filename, as_attachment=True)


@APP.route('/upload', methods=['POST'])
def upload():
    # Taken Data from the Form
    old_filename = request.form.get('oldfileName', None)
    description = request.form.get('description', None)
    new_filename = request.form.get('newfileName', None)

    # Taken Date and Username for Template
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    username = MWOAUTH.get_current_user(True)

    # Wikitext for File content
    text = "=={{int:filedesc}}==\n{{Information" + \
           "\n|description=" + description + \
           "\n|date=" + date + \
           "\n|source={{own}}" + \
           "\n|author=[[User:" + username + "|" + username + "]]" + \
           "\n}}\n\n=={{int:license-header}}==\n{{self|cc-by-sa-4.0}}"

    # Authenticate Session
    ses = authenticated_session()

    # Variable to set error state
    error = None

    if None not in (old_filename, new_filename, ses):
        # API Parameter to get CSRF Token
        csrf_param = {
            "action": "query",
            "meta": "tokens",
            "format": "json"
        }

        response = requests.get(url=API_ENDPOINT, params=csrf_param, auth=ses)
        data = response.json()
        csrf_token = data["query"]["tokens"]["csrftoken"]

        # API Parameter to upload the file
        upload_param = {
            "action": "upload",
            "filename": new_filename,
            "text": text,
            "format": "json",
            "token": csrf_token,
            "ignorewarnings": 1
        }

        # Read the file for POST request
        file = {
            'file': open('static/qrcodes/' + old_filename, 'rb')
        }

        response = requests.post(url=API_ENDPOINT, files=file, data=upload_param, auth=ses)
        data = response.json()

        # Try block to get Link and URL
        try:
            wikifile_url = data["upload"]["imageinfo"]["descriptionurl"]
            filelink = data["upload"]["imageinfo"]["url"]
        except:
            error = True
            render_template('upload.html', username=username, error=error)

        return render_template('upload.html', wikifileURL=wikifile_url, fileLink=filelink,
                               username=username, error=error)

    # If everything goes wrong append error
    error = True
    return render_template('upload.html', username=username, error=error)


def authenticated_session():
    if 'mwoauth_access_token' in session:
        auth = requests_oauthlib.OAuth1(
            client_key=CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=session['mwoauth_access_token']['key'],
            resource_owner_secret=session['mwoauth_access_token']['secret']
        )
        return auth

    return None

if __name__ == '__main__':
    APP.run()
