from flask import Flask, render_template, request, jsonify
from datetime import date, timedelta
import requests

APP = Flask(__name__)
SESSION = requests.Session()
ENDPOINT = "https://en.wikipedia.org/w/api.php"

current_date = date.today()

@APP.route("/", methods = ["GET", "POST"])

def index():
    print(request.form)
    if (request.method == "POST"):
        try:
            change_date = request.form["change_date"]

            if (change_date == "← Back"):
                new_date = decrement_date()
            elif (change_date == "Next →"):
                new_date = increment_date()
        except:
            new_date = date.today()

        current_date = new_date
        todays_date = str(current_date)
        results = fetch_potd(todays_date)

        return jsonify(results = results)

    return render_template("index.html")

def increment_date():
    return current_date + timedelta(days = 1)

def decrement_date():
    return current_date - timedelta(days = 1)

def fetch_potd(date):
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": "Template:POTD protected/" + date
    }

    response = SESSION.get(url = ENDPOINT, params = params)
    data = response.json()
    file_name = data["query"]["pages"][0]["images"][0]["title"]
    
    results = [{
        "title": file_name,
        "image": fetch_image_url(file_name),
        "description": fetch_description(params["titles"]),
        "date": date
    }]

    return results

def fetch_image_url(file_name):
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": file_name
    }

    response = SESSION.get(url = ENDPOINT, params = params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    image_info = page["imageinfo"][0]
    url = image_info["url"]

    return url

def fetch_description(page_title):
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": page_title
    }

    response = SESSION.get(url = ENDPOINT, params = params)
    data = response.json()
    results = data["query"]["search"][1]["snippet"]

    return results

if __name__ == "__main__":
    APP.run()
