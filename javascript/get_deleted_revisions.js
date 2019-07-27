/*
    get_deleted_revisions.js

    MediaWiki API Demos
    Demo of `Deletedrevs` module: List the six most recent deleted revisions from User:Catrope

    MIT License
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
        deleted_revisions();
    });
}

// Step 3: GET request to get the deleted revisions
function deleted_revisions() {
    var params_2 = {
        action: "query",
        list: "deletedrevs",
        druser: "Catrope",
        drprop: "revid|user|minor|len|token",
        drlimit: "6",
        format: "json"
    };

    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        var pages = data.query.deletedrevs;
        for (var p in pages) {
            console.log("Revision for Page " + pages[p].title);
            for (var drev in pages[p].revisions) {
                console.log(pages[p].revisions[drev]);
            }
        }
    });
}

// Start From Step 1
getLoginToken();