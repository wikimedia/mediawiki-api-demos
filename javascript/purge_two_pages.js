/*  
    purge_two_pages.js
 
    MediaWiki API Demos
    Demo of `purge` module: Sending post request to purge two or more pages

    MIT license
*/

var request = require('request').defaults({jar: true}),
    url = "https://en.wikipedia.org/w/api.php";

function purge() {
    var params = {
        action: "purge",
        titles: "Main_Page|Nonexistent",
        format: "json"
    };

    request.post({ url: url, form: params }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start the function
purge();