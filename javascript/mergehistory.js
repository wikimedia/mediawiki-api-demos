/*
    mergehistory.js

    MediaWiki API Demos
    Demo of `mergehistory` module: Merge the entire history of Oldpage to Newpage

*/
login_Token = getLoginToken(); // Step 1
loginRequest( login_Token ); // Step 2
csrf_Token = getCsrfToken(); // Step 3
mergehistory( csrf_Token ); // Step 4
var endpoint = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var request = require("request");

    var options = { 
        method: 'GET',
        url: endpoint ,
        qs: 
        { 
            action: "query",
            meta: "tokens",
            type: "login",
            format: "json"
        },
        headers: 
        { 
            'Content-Type': 'application/x-www-form-urlencoded',
            },
    };

    request(options, function (error, response, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        return data.query.tokens.logintoken;
    });
}

// Step 2: POST Request to log in. 
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var request = require("request");

    var options = { 
        method: 'POST',
        url: endpoint ,
        headers: 
        { 
            'Content-Type': 'application/x-www-form-urlencoded',
            },
        form: { 
            action: "login",
            lgname: "bot_username",
            lgpassword: "bot_password",
            lgtoken: login_token,
            format: "json" 
        } 
    };

    request(options, function (error, response, body) {
        if (error) {
            return;
        }
        getCsrfToken();
    });
}

// Step 3: GET request to fetch CSRF token
function getCsrfToken() {
    var request = require("request");

    var options = { 
        method: 'GET',
        url: endpoint ,
        qs: 
        { 
            action: "query",
            meta: "tokens",
            format: "json" 
        },
        headers: 
        { 
            'Content-Type': 'application/x-www-form-urlencoded',
            },
    };

    request(options, function (error, response, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        return data.query.tokens.csrftoken;
    });
}

// Step 4: Send a POST request to merge history of Oldpage to Newpage
function mergehistory(csrf_token) {

    var request = require("request");

    var options = { 
        method: 'POST',
        url: "https://test.wikipedia.org/w/api.php" ,
        qs: 
        { 
            action: 'mergehistory',
            from: 'Oldpage',
            to: 'Newpage',
            reason: 'Reason',
            format: 'json',
         },
        headers: 
        { 
            'Content-Type': 'application/x-www-form-urlencoded',
            },
        form: { token: csrf_token } 
    };

    request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
    });
}
