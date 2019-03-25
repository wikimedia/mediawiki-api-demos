/* 
    get_my_watchlist_feed.js
 
    MediaWiki Action API Code Samples
    Demo of `Feedwatchlist` module: Get the watchlist feed 
    for the account making the request.

    MIT license
*/
var request = require('request').defaults({jar: true}),
    url = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var params_1 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url + "?";

    Object.keys(params_1).forEach(function (key) {
        query += "&" + key + "=" + params_1[key];
    });

    request.get(query, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        loginRequest(data.query.tokens.logintoken);
    });
}

// Step2: Send a post request to login. Use of main account for login is not
//  supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_2 = {
        action: "login",
        lgname: "bot_username",
        lgpassword: "bot_password",
        lgtoken: login_token,
        format: "json"
    };

    request.post({
        url: url, 
        form: params_2,
    }, function(error, res, body) {
        if (error) {
            return;
        }
        getWatchlistFeed();
    });
}

// Step 3: Request the account's own watchlist feed
function getWatchlistFeed() {
    var params_3 = {
        action: "feedwatchlist"
    };

    var query = url + "?";

    Object.keys(params_3).forEach(function (key) {
        query += "&" + key + "=" + params_3[key];
    });

    request.get(query, function(error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getLoginToken();