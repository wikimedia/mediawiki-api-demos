#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask, render_template, request, Markup, send_from_directory
import qrcode
import qrcode.image.svg
import datetime
import urllib

app = Flask( __name__ )


@app.route('/', methods=['GET'])
def index():

    # Get the URL from the query string
    url = request.args.get('urltextBox')

    if url is None:
        return render_template('Index.html')
    else:

        # Escape the unicode encoding from URL
        url = urllib.parse.unquote(url)

        # Get the file name based on current time
        currentTime = str(datetime.datetime.now())
        getfileName = currentTime.replace(':', '_').replace(' ', '_') + '.svg'
        fileWithPath = 'static/qrcodes/' + getfileName

        # Create the QR Code
        img = qrcode.make( url, image_factory=qrcode.image.svg.SvgImage, version=8 )
        img.save(fileWithPath)

        # Read the QR Code
        svg = open(fileWithPath).read()

        return render_template( 'Index.html', url=url, fileName=getfileName, src= Markup(svg) )


@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    return send_from_directory( directory='static/qrcodes', filename=filename, as_attachment=True)


if __name__ == '__main__':
    app.run()