/*  
    userrights.js
 
    MediaWiki API Demos
    Demo of `Userrights` module: Add and remove user rights by
	changing the user's group membership.

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
        getUserRightsToken();
    });
}

// Step 3: GET request to fetch UserRights token
function getUserRightsToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        type: "userrights",
        format: "json"
    };

    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        userrights(data.query.tokens.userrightstoken);
    });
}

// Step 4: POST request to add or remove a user from a group
function userrights(userrights_token) {
    var params_3 = {
        action: "userrights",
        user: "ABCDEFG",
        add: "bot",
        expiry: "infinite",
        reason: "API Testing",
        token: userrights_token,
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