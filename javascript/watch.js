
//Function to convert the dictionary element as an encoded URL

function conv(parm) {
  var str = [];
  for(var p in parm)
     str.push(encodeURIComponent(p) + "=" + encodeURIComponent(parm[p]));
  return str.join("&");
}
const URL = "https://test.wikipedia.org/w/api.php";

//Retrieve login token first

var PARAMS_1 = {'action':"query",'meta':"tokens",'type':"login",'format':"json"};
var url = URL+"?"+conv(PARAMS_1);
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
/*# Step 2: Send a post request to log in. For this loginmethod, Obtain credentials by first visiting
https://www.en.wikipedia.org/wiki/Special:BotPasswords
See https://www.mediawiki.org/wiki/API:Login for more information on log in methods.*/

var PARAMS_2 = {'action':"login",'lgname':"username",'lgpassword':"password",'format':"json",'lgtoken':LOGIN_TOKEN};
var S1 = new XMLHttpRequest();
S1.open("POST",URL);
S1.setRequestHeader("Content-type","application/x-www-form-urlencoded");
S1.send(conv(PARAMS_2));  //Sending POST request with encoded elements
S1.onreadystatechange = function(){
     if(S1.status==200 && S1.readyState==4){
	      //Step 3: While logged in, retrieve a CSRF token
		  
          var PARAMS_3 = {"action": "query","meta": "tokens","type": "watch","format": "json"};
          var url = URL+"?"+conv(PARAMS_3);
          var S2 = new XMLHttpRequest();
          S2.open("GET",url);
          S2.send();
          S2.onreadystatechange = function(){
                 if(S2.status==200 && S2.readyState==4){
	             var R = S2.responseText;
		         var DATA = JSON.parse(R);
		         var CSRF_TOKEN = DATA.query.tokens.watchtoken;
	            }
            };
			//Step 4: Post request to add a page to your watchlist
			
			PARAMS_4 = {"action": "watch","titles": "Stone forest","format": "json","token": CSRF_TOKEN,};
			var S3 = new XMLHttpRequest();
			S3.open("POST",URL);
            S3.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            S3.send(conv(PARAMS_4));  //Sending POST request with encoded elements
			S3.onreadystatechange = function(){
				if(S1.status==200 && S1.readyState==4){
					var R = S3.responseText;
					var DATA = JSON.parse(R);
					console.log(DATA);
				}
			}
	    }
    };
