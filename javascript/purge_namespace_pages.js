/*  
    purge_namespace_pages.js
 
    MediaWiki API Demos
    Demo of `purge` module: Sending post request to purge first 10 pages in the main namespace

    MIT license
*/

var request = require('request').defaults({jar: true}),
    url = "https://test.wikipedia.org/w/api.php";

function purge() {
    var params = {
        action: "purge",
        generator: "allpages",
        gapnamespace: "0",
        gaplimit: "10",
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