# Article Suggestion
A sample app that uses MediaWiki Action [API:Search](https://www.mediawiki.org/wiki/API:Search) allows you to pick a category and suggest articles to write on that don't yet exist on English Wikipedia. This app uses Flask and [WTForms](https://wtforms.readthedocs.io/en/stable/) for rendering form.

Articles in the `articles.json` file are taken from the link below:
https://en.wikipedia.org/wiki/Wikipedia:Requested_articles/Biography/By_profession

Install
-------

```
$ git clone https://github.com/srish/MediaWiki_Action_API_Code_Samples
$ cd MediaWiki-Action-API-Code-Samples/python/demos/article suggestion
$ pip install flask flask-WTF flask-bootstrap
Install the necessary python modules with pip
$ python3 app.py
```

Screenshot
----------

<table><tr><td>
<img src="screenshot.png" width="300" style="border 5px solid black">
</td></tr></table>
