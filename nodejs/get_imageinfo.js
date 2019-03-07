/*
    get_imageinfo.js

    MediaWiki Action API Code Samples
    Demo of `Imageinfo` module: Get information about an image file.
    MIT license
*/

let request = require('request');

let URL = "https://en.wikipedia.org/w/api.php";

let PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Billy_Tipton.jpg"
}

request.get( { url: URL, qs: PARAMS }, function( error, response, body ){
        console.log( body );
    }
);