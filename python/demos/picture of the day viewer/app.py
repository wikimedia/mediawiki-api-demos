"""
    App.py
    MediaWiki Action API Code Samples

    Fetches the current Wikipedia Picture of the Day (POTD) and displays it on
    a webpage. Also allows for user to change the date displayed.

    Attributes
    ----------
        change_date(): Alter current date displayed
        increment(date_object): Next date
        decrement(date_object): Previous date
        index(): Render web page with current POTD
        potd_json(date_object): Create JSON from fetch_potd(day)
        fetch_potd(day): Fetch data about current picture from POTD endpoint
        fetch_image_info(file_name): Fetchs image & description url

    MIT License
"""

#!/usr/bin/python3

from datetime import date, timedelta
from flask import Flask, render_template, request, jsonify, redirect
import requests

APP = Flask(__name__)
SESSION = requests.Session()
ENDPOINT = "https://en.wikipedia.org/w/api.php"
CURRENT_DATE = date.today()

@APP.route("/change_date", methods=["POST"])

def change_date():
    """
    Alter CURRENT_DATE in response to user input, thus changing the POTD
    being displayed on the webpage.

    Returns
    -------
    Response object
        A redirect to the index path, forcing the page to re-render with
        the POTD for the updated CURRENT_DATE.
    """

    global CURRENT_DATE

    user_input = request.form["change_date"]
    new_date = CURRENT_DATE

    if user_input == "← Back":
        new_date = decrement(new_date)
    elif user_input == "Next →":
        new_date = increment(new_date)

    CURRENT_DATE = new_date

    return redirect("/")

def increment(date_object):
    """Returns the next date for a date object (i.e. tomorrow)"""

    return date_object + timedelta(days=1)

def decrement(date_object):
    """Returns the previous date for a date object (i.e. yesterday)"""

    return date_object - timedelta(days=1)

@APP.route("/", methods=["GET", "POST"])

def index():
    """
    Requests data from the WikiMedia Action API, related to the POTD for
    the CURRENT_DATE, and renders it on a webpage located at the index path.

    Returns
    -------
    JSON data related to the current POTD, if POST request.
    Renders the webpage, templates/index.html, otherwise.
    """
    if request.method == "POST":
        return potd_json(CURRENT_DATE)

    return render_template("index.html")

def potd_json(date_object):
    """Returns JSON formated data for the current POTD"""

    results = fetch_potd(date_object)

    return jsonify(results=results)

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

    day = date_object.isoformat()

    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": "Template:POTD protected/" + day
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()

    file_name = data["query"]["pages"][0]["images"][0]["title"]
    image_info = fetch_image_info(file_name)
    formatted_day = date_object.strftime("%x")

    results = [{
        "title": file_name,
        "image": image_info["image_url"],
        "description": image_info["description_url"],
        "date": formatted_day
    }]

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
        Data detailing the POTD's image url and description url.
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
    description_url = image_info["descriptionurl"]

    results = {
        "image_url": image_url,
        "description_url": description_url
    }

    return results

if __name__ == "__main__":
    APP.run()