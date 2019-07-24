/*  
    rollback.js
 
    MediaWiki API Demos
    Demo of `rollback` module: Sending post request to rollback the
    edits of a given page.

    MIT license
*/

var request = require('request').defaults({jar: true}),
    url = "http://dev.wiki.local.wmftest.net:8080/w/api.php";

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

    request.post({ url: url, form: params_1 }, function (error, res, body) {
        if (error) {
            return;
        }
        getRollbackToken();
    });
}

// Step 3: GET request to fetch Rollback token
function getRollbackToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        type: "rollback",
        format: "json"
    };

    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        rollback(data.query.tokens.rollbacktoken);
    });
}

// Step 4: POST request to rollback a page
function rollback(rollback_token) {
    var params_3 = {
        action: "rollback",
        title: "Sandbox",
        user: "10.0.2.2",
        token: rollback_token,
        format: "json"
    };

    request.post({ url: url, form: params_3 }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getLoginToken();