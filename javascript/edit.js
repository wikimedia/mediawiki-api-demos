/**  
 edit.js
 
 MediaWiki Action API Code Samples
 Demo of `Edit` module: POST request to edit a page
 MIT license
*/

var url = "https://test.wikipedia.org/w/api.php";
url = url + "?";

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var params_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url;
    Object.keys(params_0).forEach(function (key) {
        query += "&" + key + "=" + params_0[key];
    });

    fetch(query, {
            method: "GET",
            credentials: "include",
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            loginRequest(data.query.tokens.logintoken);
        })
        .catch(function (error) {
            console.log(error);
        });
}

// Step 2: POST Request to log in. 
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_1 = {
        action: "login",
        lgname: "bot_user_name",
        lgpassword: "bot_password",
        lgtoken: login_token,
        format: "json"
    };

    console.log(params_1);

    fetch(url, {
            method: "POST",
            body: JSON.stringify(params_1),
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            getCsrfToken();
        })
        .catch(function (error) {
            console.log(error);
        });
}

// Step 3: GET request to fetch CSRF token
function getCsrfToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        format: "json"
    };

    var query = url;
    Object.keys(params_2).forEach(function (key) {
        query += "&" + key + "=" + params_2[key];
    });

    fetch(query, {
            method: "GET",
            credentials: "include",
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            editRequest(data.query.tokens.csrftoken);
        })
        .catch(function (error) {
            console.log(error);
        });
}

// Step 4: POST request to edit a page
function editRequest(csrf_token) {
    var params_3 = {
        action: "edit",
        title: "Sandbox",
        token: csrf_token,
        format: "json",
        appendtext: "Hello"
    };

    fetch(url, {
            method: "POST",
            body: JSON.stringify(params_3),
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
}

// Start From Step 1
getLoginToken();