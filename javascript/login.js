/*
    login.js
    MediaWiki Action API Code Samples
    Demo of `Login` module: Sending post request to login
    MIT license
*/

//Function to convert the dictionary element as an encoded URL

function conv(parm) {
  var str = [];
  for(var p in parm)
     str.push(encodeURIComponent(p) + "=" + encodeURIComponent(parm[p]));
  return str.join("&");
}
const URL = "https://mediawiki.org/w/api.php";

//Retrieve login token first

var PARAMS_0 = {'action':"query",'meta':"tokens",'type':"login",'format':"json"};
var url = URL+"?"+conv(PARAMS_0);
var S = new XMLHttpRequest();
S.open("GET",url);
S.send();
S.onreadystatechange = function(){
     if(S.status==200 && S.readyState==4){
	      var R = S.responseText;
		  var DATA = JSON.parse(R);
		  var LOGIN_TOKEN = DATA.query.tokens.logintoken;
		  console.log(LOGIN_TOKEN);
	 }
};

/*Send a post request to login. Using the main account for login is not supported. 
Obtain credentials via Special:BotPasswords(https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword*/

var PARAMS_1 = {'action':"login",'lgname':"your_bot_username",'lgpassword':"your_bot_password",'lgtoken':LOGIN_TOKEN,'format':"json"};
var S1 = new XMLHttpRequest();
S1.open("POST",URL);
S1.setRequestHeader("Content-type","application/x-www-form-urlencoded");
S1.send(conv(PARAMS_1));  //Sending POST request with encoded elements
S1.onreadystatechange = function(){
     if(S1.status==200 && S1.readyState==4){
	      var R = S1.responseText;
		  var DATA = JSON.parse(R);
		  console.log(DATA);
	 }
};
