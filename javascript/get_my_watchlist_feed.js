"use strict";

/** 
 * get_my_watchlist_feed.js
 *
 * MediaWiki Action API Code Samples
 * Demo of `Feedwatchlist` module: Get the watchlist feed 
 * for the account making the request.
 * MIT license
 */
const fetch = require("node-fetch");

let URL = "https://test.wikipedia.org/w/api.php"

async function main() {
   // Step 1: GET Request to fetch login token
   const PARAMS_1 = {
       action: "query",
       meta: "tokens",
       type: "login",
       format: "json"
   }
   
   let query = URL + '?' + Object.keys(PARAMS_1).map(key => key + "=" + PARAMS_1[key]).join("&");
   let response = await fetch(query);
   let data = await response.json();

   let LOGIN_TOKEN = data.query.tokens.logintoken;

   // Step2: Send a post request to login. Use of main account for login is not
   //  supported. Obtain credentials via Special:BotPasswords
   // (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
   const PARAMS_2 = {
       action: "login",
       lgname: "your_bot_username",
       lgpassword: "your_bot_password",
       lgtoken: LOGIN_TOKEN,
       format: "json"
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
       action: "feedwatchlist"
   }

   query = URL + '?' + Object.keys(PARAMS_3).map(key => key + "=" + PARAMS_3[key]).join("&");
   response = await fetch(query);
   data = await response.text();

    console.log(data);
}    

main();