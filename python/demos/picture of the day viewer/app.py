"""
    app.py
    MediaWiki Action API Code Samples

    Fetches Wikipedia Picture of the Day (POTD) and displays it on
    a webpage. Also allows to go backward or foward a date to view other Pictures of the Day in the Wikipedia archives.

    MIT License
"""

#!/usr/bin/python3

from datetime import date, timedelta
from flask import Flask, render_template, request
import requests


APP = Flask(__name__)
SESSION = requests.Session()
ENDPOINT = "https://en.wikipedia.org/w/api.php"
_current_date = date.today()

@APP.route("/", methods=["GET", "POST"])
def index():
    """
    Requests data from the Action API & renders it on a webpage.
    """

    global _current_date

    if request.method == "POST":
        _current_date = change(_current_date)

    data = fetch_potd(_current_date)

    return render_template("index.html", data=data)


def change(date_object):
    """
    Return new date in response to input from the web form.
    """

    user_input = request.form["change_date"]
    new_date = _current_date
    last_date = date.today()
    first_date = date(year=2004, month=5, day=14)

    if user_input == "← Back":
        new_date = new_date - timedelta(days=1)
    elif user_input == "Next →":
        new_date = new_date + timedelta(days=1)

    if new_date > last_date or new_date < first_date:
        return _current_date

    return new_date


def fetch_potd(date_object):
    """
    Returns image data related to the current POTD.
    """

    date_string = date_object.isoformat()
    title = "Template:POTD protected/" + date_string

    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": title
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()

    filename = data["query"]["pages"][0]["images"][0]["title"]
    image_src = fetch_image_src(filename)
    image_page_url = "https://en.wikipedia.org/wiki/Template:POTD_protected/" + date_string

    results = {
        "filename": filename,
        "image_src": image_src,
        "image_page_url": image_page_url,
        "date": date_object
    }

    return results


def fetch_image_src(filename):
    """
    Returns the POTD's image url.
    """

    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": filename
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    image_info = page["imageinfo"][0]
    results = image_info["url"]

    return results


if __name__ == "__main__":
    APP.run()
