/*
    stashedit.js

    MediaWiki API Demos
    Demo of `stashedit` module: prepare an edit in shared cache

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

// Step 2: Send a post request to log in using the clientlogin method.
// import rights can't be granted using Special:BotPasswords
// hence using bot passwords may not work.
// See https://www.mediawiki.org/wiki/API:Login for more
// information on log in methods.
function loginRequest(login_token) {
    var params_1 = {
        action: "clientlogin",
        username: "username",
        password: "password",
        loginreturnurl: "http://127.0.0.1:5000/",
        logintoken: login_token,
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

// Step 4: Send a POST request  to prepare an edit in shared cache
function stashEdit(csrf_token) {
    var params_3 = {
        action: "stashedit",
        title: "User:Zaycodes/Sandbox/API:Mergehistory",
        section: "new",
        sectiontitle: "testing stashedit",
        text: "testing stashedit API",
        contentmodel: "text",
        contentformat: "text/plain",
        baserevid: 1,
        format: "json",
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


