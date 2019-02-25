"""
    App.py
    MediaWiki Action API Code Samples

    Fetches the current Wikipedia Picture of the Day (POTD) and displays it on
    a webpage. Also allows for user to change the date displayed.

    Attributes
    ----------
        change(date_object): Alter current date displayed
        increment(date_object): Next date
        decrement(date_object): Previous date
        index(): Render web page with current POTD
        fetch_potd(day): Fetch data about current picture from POTD endpoint
        fetch_image_info(file_name): Fetchs image & description url

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
    Requests data from the WikiMedia Action API, related to the POTD for
    the _current_date, and renders it on a webpage located at the index path.

    Returns
    -------
    JSON data related to the current POTD, if POST request.
    Renders the webpage, templates/index.html, otherwise.
    """

    global _current_date

    if request.method == "POST":
        _current_date = change(_current_date)

    data = fetch_potd(_current_date)

    return render_template("index.html", data=data)


def change(date_object):
    """
    Return new date in response to user input, thus changing the POTD
    being displayed on the webpage.
    """

    user_input = request.form["change_date"]
    new_date = _current_date
    last_date = date.today()
    first_date = date(year=2004, month=5, day=14)

    if user_input == "← Back" and decrement(new_date) > first_date:
        new_date = decrement(new_date)
    elif user_input == "Next →" and increment(new_date) <= last_date:
        new_date = increment(new_date)

    return new_date

def increment(date_object):
    """Returns the next date for a date object (i.e. tomorrow)"""

    return date_object + timedelta(days=1)

def decrement(date_object):
    """Returns the previous date for a date object (i.e. yesterday)"""

    return date_object - timedelta(days=1)


def fetch_potd(date_object):
    """
    Returns image data related to the current POTD.

    Parameters
    ----------
    date_object: date
        A datetime.date object, used to construct a title in order to find the
        correct POTD in the POTD archives.

    Returns
    -------
    list[dict]
        JSON detailing the POTD's filename, image url, description url, and the
        date it was featured as Picture of the Day.
    """

    date_string = date_object.isoformat()

    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": "Template:POTD protected/" + date_string
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()

    file_name = data["query"]["pages"][0]["images"][0]["title"]
    image_info = fetch_image_info(file_name)

    results = {
        "title": file_name,
        "image_src": image_info,
        "image_page": "https://en.wikipedia.org/wiki/Template:POTD_protected/" + date_string,
        "date": date_object
    }

    return results

def fetch_image_info(file_name):
    """
    Returns the POTD's image url & image description.

    Parameters
    ----------
    File_name: String
        The name of the image file for the POTD.

    Returns
    -------
    list[dict]
        The POTD's image url and description url.
    """

    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": file_name
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    image_info = page["imageinfo"][0]
    image_url = image_info["url"]

    results = image_url

    return results

if __name__ == "__main__":
    APP.run()
