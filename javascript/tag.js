/*
    tag.js

    MediaWiki API Demos
    Demo of `Tag` module: Remove the spam tag from log entry ID 123 with the reason Wrongly applied

    MIT license
*/
var request = require("request").defaults({jar: true}),
url = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var params_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };
    request.get({ url: url, qs: params_0 }, function (error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        loginRequest(data.query.tokens.logintoken);
    });
}

// Step 2: POST request to log in. 
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_1 = {
        action: "login",
        lgname: "bot_username",
        lgpassword: "bot_password",
        lgtoken: login_token,
        format: "json"
    };
    
    request.post({ url: url, form: params_1 }, function (error, res, body) {
        if (error) {
            return;
        }
        getCsrfToken();
    });
}

// Step 3: GET request to fetch CSRF token
function getCsrfToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        format: "json"
    };
    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        stashEdit(data.query.tokens.csrftoken);
    });
}

// Step 4: remove the spam tag from log entry ID 123 with the reason Wrongly applied
function stashEdit(csrf_token) {
    var params_3 = {
        action: "compare",
        format: "json",
        token: csrf_token,
        logid: "123",
        remove: "spam",
        reason: "Wrongly applied"
    };
    request.post({ url: url, form: params_3 }, function(error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getLoginToken();


