/*  
    edit.js
 
    MediaWiki Action API Code Samples
    Demo of `Edit` module: POST request to edit a page

    MIT license
*/

var request = require('request').defaults({jar: true}),
    url = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
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

// Step 2: POST Request to log in. 
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

// Step 3: GET request to fetch CSRF token
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
        editRequest(data.query.tokens.csrftoken);
    });
}

// Step 4: POST request to edit a page
function editRequest(csrf_token) {
    var params_3 = {
        action: "edit",
        title: "Sandbox",
        token: csrf_token,
        format: "json",
        appendtext: "test edit"
    };

    request.post({
        url: url, 
        form: params_3,
    }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getLoginToken();