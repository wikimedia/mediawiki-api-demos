/*
    get_all_deleted_revisions.js

    MediaWiki API Demos
    Demo of `alldeletedrevisions` module: List all the deleted revisions from User:mahesh

    MIT License
*/

var request = require('request').defaults({jar: true}),
    url = "https://www.thetestwiki.org/w/api.php";

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
        all_deleted_revisions();
    });
}

// Step 3: GET request to get the deleted revisions
function all_deleted_revisions() {
    var params_2 = {
        action: "query",
        list: "alldeletedrevisions",
        adruser: "Mahesh",
        adrprop: "ids|user|comment",
        format: "json"
    };

    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        var pages = data.query.alldeletedrevisions;
        for (var p in pages) {
            console.log("Revision for Page " + pages[p].title);
            for (var adrev in pages[p].revisions) {
                console.log(pages[p].revisions[adrev]);
            }
        }
    });
}

// Start From Step 1
getLoginToken();
