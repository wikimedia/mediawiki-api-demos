/*
    logout.js

    MediaWiki API Demos
    Demo of `Logout` module: Log out and clear session data.

    MIT License
*/

var request = require('request').defaults({jar: true}),
    url = "https://en.wikipedia.org/w/api.php";

// Retrieve login token first
function getLoginToken() {
    var params_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url + "?";

    Object.keys(params_0).forEach(function (key) {
        query += "&" + key + "=" + params_0[key];
    });

    request.get(query, function (error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        loginRequest(data.query.tokens.logintoken);
    });
}

// POST Request to login
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_1 = {
        action: "login",
        lgname: "your_bot_username",
        lgpassword: "your_bot_password",
        lgtoken: login_token,
        format: "json"
    };

    request.post({
        url: url,
        form: params_1,
    }, function (error, res, body) {
        if (error) {
            return;
        }
        getCsrfToken();
    });
}

// GET request to fetch CSRF token
function getCsrfToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        format: "json"
    };

    var query = url + "?";

    Object.keys(params_2).forEach(function (key) {
        query += "&" + key + "=" + params_2[key];
    });

    request.get(query, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        logoutRequest(data.query.tokens.csrftoken);
    });
}

// Send a POST request to logout
function logoutRequest(csrf_token) {
    var params_3 = {
        action: "logout",
        token: csrf_token,
        format: "json"
    };

    request.post({
        url: url,
        form: params_3,
    }, function (error, res, body) {
        if (error) {
            return;
        }

        // Check weither the response is null or not
        if ( body == '{}' ){
            console.log("You have successfully logout.");
        }
    });
}

// Start From Step 1
getLoginToken();