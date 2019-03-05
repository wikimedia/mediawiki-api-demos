/*
    get_my_watchlist_feed.js
    MediaWiki Action API Code Samples
    Demo of `Feedwatchlist` module: Get the watchlist feed 
    for the account making the request.
    MIT license
*/

let URL = "https://test.wikipedia.org/w/api.php"

function get_query(url, params) {
   let query = Object.keys(params).map(key => key + "=" + params[key]).join("&");
   return url + "?" + query;
}

async function get_my_watchlist_feed() {
   // Step 1: GET Request to fetch login token
   const PARAMS_1 = {
       'action': "query",
       'meta': "tokens",
       'type': "login",
       'format': "json"
   }

   let response = await fetch(get_query(URL, PARAMS_1));
   let data = await response.json();
   let LOGIN_TOKEN = data['query']['tokens']['logintoken'];

   // Step2: Send a post request to login. Use of main account for login is not
   //  supported. Obtain credentials via Special:BotPasswords
   // (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
   const PARAMS_2 = {
       'action': "login",
       'lgname': "your_bot_username",
       'lgpassword': "your_bot_password",
       'lgtoken': LOGIN_TOKEN,
       'format': "json"
   }

    response = await fetch(URL, {
       method: 'POST',
       body: JSON.stringify(PARAMS_2),
       headers: {
           'Content-Type': 'application/json'
       }
   });

    // Step 3: Request the account's own watchlist feed
   const PARAMS_3 = {
       "action": "feedwatchlist"
   }

    response = await fetch(get_query(URL, PARAMS_3));
   data = await response.text;

    console.log(data);
}    

get_my_watchlist_feed();