from flask import Flask, request, jsonify, render_template
from datetime import date
import requests

APP = Flask(__name__)
SESSION = requests.Session()
ENDPOINT = "https://en.wikipedia.org/w/api.php"

@APP.route("/", methods = ["GET", "POST"])

def index():
    if (request.method == "POST"):
        todays_date = str(date.today())
        results = fetch_potd(todays_date)

        return jsonify(results = results)

    return render_template("index.html")

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
    file_name = data["query"]["pages"][0]['images'][0]['title']
    
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
    image_info = page['imageinfo'][0]
    url = image_info['url']

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

if __name__ == '__main__':
    APP.run()
