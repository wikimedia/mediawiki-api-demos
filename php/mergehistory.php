<?php

/*
    mergehistory.php

    MediaWiki API Demos
    Demo of `mergehistory` module: Merge the page revisions of Oldpage 
	dating up to 2015-12-31T04:37:41Z into Newpage
	
	MIT license
*/
$endPoint = "https://test.wikipedia.org/w/api.php";

$login_Token = getLoginToken(); // Step 1
loginRequest( $login_Token ); // Step 2
$csrf_Token = getCSRFToken(); // Step 3
mergehistory( $csrf_Token ); // Step 4

// Step 1: GET request to fetch login token
function getLoginToken() {
	global $endPoint;

	$params1 = [
		"action" => "query",
		"meta" => "tokens",
		"type" => "login",
		"format" => "json"
	];

	$url = $endPoint . "?" . http_build_query( $params1 );

	$ch = curl_init( $url );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

	$result = json_decode( $output, true );
	return $result["query"]["tokens"]["logintoken"];
}

// Step 2: Send a post request to log in using the clientlogin method.
// import rights can't be granted using Special:BotPasswords
// hence using bot passwords may not work.
// See https://www.mediawiki.org/wiki/API:Login for more
// information on log in methods.
function loginRequest( $logintoken ) {
	global $endPoint;

	$params2 = [
		"action" => "clientlogin",
		"username" => "username",
		"password" => "password",
		'loginreturnurl' => 'http://127.0.0.1:5000/',
		"logintoken" => $logintoken,
		"format" => "json"
	];

	$ch = curl_init();

	curl_setopt( $ch, CURLOPT_URL, $endPoint );
	curl_setopt( $ch, CURLOPT_POST, true );
	curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params2 ) );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );
}

// Step 3: GET request to fetch CSRF token
function getCSRFToken() {
	global $endPoint;

	$params3 = [
		"action" => "query",
		"meta" => "tokens",
		"format" => "json"
	];

	$url = $endPoint . "?" . http_build_query( $params3 );

	$ch = curl_init( $url );

	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

	$result = json_decode( $output, true );
	return $result["query"]["tokens"]["csrftoken"];
}

# Step 4: Send a POST request  to merge the page revisions of Oldpage dating up to 2015-12-31T04:37:41Z into Newpage
function mergeHistory( $csrftoken ) {
	global $endPoint;
	
	$params4 = [
		"action"=>"mergehistory",
		"from"=>"Oldpage",
		"to"=>"Newpage",
		"format"=>"json",
		"timestamp"=>"2015-12-31T04:37:41Z",
		"reason"=>"Reason",
		"token" => $csrftoken
	];
  
	$ch = curl_init();

	curl_setopt( $ch, CURLOPT_URL, $endPoint );
	curl_setopt( $ch, CURLOPT_POST, true );
	curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params4 ) );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$response = curl_exec($ch);
	curl_close($ch);

	echo ($response);
}

/*
    To merge entire history of Oldpage to Newpage,
    remove the "timestamp" parameter in step 4

*/
