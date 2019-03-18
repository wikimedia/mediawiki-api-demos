/* 
 get_my_watchlist_feed.js
 
 MediaWiki Action API Code Samples
 Demo of `Feedwatchlist` module: Get the watchlist feed 
 for the account making the request.
 MIT license
*/
var url = "https://test.wikipedia.org/w/api.php";
url = url  + '?';

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var params_1 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url;

    Object.keys(params_1).forEach(function (key) {
        query += "&" + key + "=" + params_1[key];
    });

    fetch(query)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            loginRequest(data.query.tokens.logintoken);
        });

}

// Step2: Send a post request to login. Use of main account for login is not
//  supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_2 = {
        action: "login",
        lgname: "bot_user_name",
        lgpassword: "bot_password",
        lgtoken: login_token,
        format: "json"
    };
    fetch(url, {
            credentials: "include",
            method: "POST",
            body: JSON.stringify(params_2),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(function () {
            getAccountFeed();
        })
        .catch(function (error) {
            console.log(error);
        });
}

// Step 3: Request the account's own watchlist feed
function getAccountFeed() {
    var params_3 = {
        action: "feedwatchlist"
    };

    var query = url;
    Object.keys(params_3).forEach(function (key) {
        query += "&" + key + "=" + params_3[key];
    });
    fetch(query, {
            credentials: "include",
        })
        .then(function (response) {
            return response.text();
        })
        .then(function (data) {
            console.log(data);
        });
}

// Start From Step 1
getLoginToken();