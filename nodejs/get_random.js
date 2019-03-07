/*
    get_random.js

    MediaWiki Action API Code Samples
    Demo of `Random` module: Get request to list 5 random pages.
    MIT license
*/

let request = require('request');

let URL = "https://en.wikipedia.org/w/api.php";

let PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "5"
}

request.get( { url: URL, qs: PARAMS }, function( error, response, body ){
        console.log( body );
    }
);