/*
    revision_delete.js

    MediaWiki API Demos
    Demo of `Revisiondelete` module: Hide all information about a certain revision ID.

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

// Step 2: Send a POST request to log in. For this login
// method, obtain credentials by first visiting
// https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
// See https://www.mediawiki.org/wiki/API:Login for more
// information on log in methods.
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
        mergeHistory(data.query.tokens.csrftoken);
    });
}

// Step 4: Send a POST request to hide all information about a certain revision ID.
function mergeHistory(csrf_token) {
    var params_3 = {
        action:"revisiondelete",
        type:"revision",
        ids:"71",
        format:"json",
        hide:"content|comment|user",
        reason:"Because",
        token: csrf_token
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
