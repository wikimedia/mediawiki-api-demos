/*  
    create_account.js
 
    MediaWiki API Demos
    Demo of `createaccount` module: Create an account on a wiki without the
    special authentication extensions

    MIT license
*/

var request = require('request').defaults({jar: true}),
    wikiUrl = "http://dev.wiki.local.wmftest.net:8080",
    endPoint = wikiUrl + "/w/api.php";

// Step 1: GET Request to fetch createaccount token
function getCreateAccountToken() {
    var params_0 = {
        action: "query",
        meta: "tokens",
        type: "createaccount",
        format: "json"
    };

    request.get({ url: endPoint, qs: params_0 }, function (error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        createaccount(data.query.tokens.createaccounttoken);
    });
}

// Step 2: POST Request with the fetched token and other data (user information,
// return URL, etc.)  to the API to create an account
function createaccount(createaccount_token) {
    var params_1 = {
        action: "createaccount",
        username: "your_username",
        password: "your_password",
        retype: "retype_your_password",
        createreturnurl: wikiUrl,
        createtoken: createaccount_token,
        format: "json"
    };

    request.post({ url: endPoint, form: params_1 }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getCreateAccountToken();