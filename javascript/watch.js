/*
watch.js
    MediaWiki Action API Code Samples
    Demo of `Watch` module: Add a page to your watchlist
    MIT license
*/
var fetch = require('node-fetch');
var url = "https://en.wikipedia.org/w/api.php";
url = url + "?";
var cookie;

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var PARAMS_1 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url;
    Object.keys(PARAMS_1).forEach(function (key) {
        query += "&" + key + "=" + PARAMS_1[key];
    });

    fetch(query)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            doLogin(data.query.tokens.logintoken);
        })
        .catch(function (error) {
            console.log(error);
        });
}
/*Step 2: Send a post request to log in. For this login method, Obtain credentials by first visiting https://www.en.wikipedia.org/wiki/Special:BotPasswords
See https://www.mediawiki.org/wiki/API:Login for more information on log in methods.*/
function doLogin(LOGIN_TOKEN){
	var PARAMS_2 = {
    action:"login",
    lgname:"your_bot_username",
    lgpassword:"your_bot_password",
    lgtoken:LOGIN_TOKEN,
    format:"json"
};
  fetch(url,{credentials:"include",
              method:"POST",
			  body:JSON.stringify(PARAMS_2),
			  header:{
				  "Content-type":"application/json"
			  }
  })
  .then(function(response){
	  var setCookie = response.headers.get('set-cookie');
      cookie = setCookie.substr(0, setCookie.indexOf(';'));
	  getCsrfToken();
  })
  .catch(function (error){
	  console.log(error);
  });
  }
  //retrieve a CSRF token
 function getCsrfToken(){
	 var PARAMS_3 = {
    action: "query",
    meta: "tokens",
    type: "watch",
    format: "json"
};
  var query = url;
    Object.keys(PARAMS_3).forEach(function (key) {
        query += "&" + key + "=" + PARAMS_3[key];
    });
	fetch(query, {
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "Cookie": cookie,
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            addPage(data.query.tokens.watchtoken);
        })
        .catch(function (error) {
            console.log(error);
        });
 }
 //Post request to add a page to your watchlist
 function addPage(CSRF_TOKEN){
	 var PARAMS_4 = {
    action: "watch",
    titles: "Stone forest",
    format: "json",
    token: CSRF_TOKEN,
}
fetch(url,{credentials: "include",
            method: "POST",
            body: JSON.stringify(PARAMS_4),
            headers: {
                "Content-Type": "application/json",
                "Cookie": cookie,
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
