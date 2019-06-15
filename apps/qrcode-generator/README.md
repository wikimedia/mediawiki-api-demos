# QR Code Generator
This is a QRCode generator for Wikimedia Sites. This app uses the MediaWiki OAuth Python library [flask-mwoauth](https://github.com/valhallasw/flask-mwoauth) for authentication and [Action API](https://www.mediawiki.org/wiki/API:Main_page) [Upload](https://www.mediawiki.org/wiki/API:Upload) for uploading the generated QR codes to Wikimedia Commons.

Install
-------

```
$ git clone https://github.com/Jayprakash-SE/qrcode-generator.git
$ pip3 install -r requirements.txt
$ python3 app.py
```

Screenshot
----------

<table><tr><td>
<img src="screenshot.png" width="300" style="border 5px solid black">
</td></tr></table>