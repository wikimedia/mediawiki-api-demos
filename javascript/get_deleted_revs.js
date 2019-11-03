/*
    get_deleted_revs.js

    MediaWiki API Demos
    Demo of `Deleted revisions:Get a list of deleted revision for Talk:Main Page` module

    MIT License
*/

var request = require('request').defaults({jar: true}),
    url = "https://en.wikipedia.org/w/api.php";

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

// Step 3: GET request to get a list of deleted revisions

var url = "https://en.wikipedia.org/w/api.php"; 

var params_2 = {
    action: "query",
    format: "json",
    titles: "Talk:MainPage",
    prop:   "deletedrevisions",
    drv:    "prop"
};

url = url + "?origin=*";
Object.keys(params_2).forEach(function(key){url += "&" + key + "=" + params_2[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error){console.log(error);});
