<?php

/*
    mergehistorytimestamp.php

    MediaWiki API Demos
    Demo of `mergehistory` module: Merge the page revisions of Oldpage 
    dating up to 2015-12-31T04:37:41Z into Newpage

*/
$endPoint = "https://test.wikipedia.org/w/api.php";

$login_Token = getLoginToken(); // Step 1
loginRequest( $login_Token ); // Step 2
$csrf_Token = getCSRFToken(); // Step 3
mergehistorytimestamp( $csrf_Token ); // Step 4

// Step 1: GET Request to fetch login token
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
  curl_setopt_array($ch, array(
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_COOKIEJAR =>  "cookie.txt",
    CURLOPT_COOKIEFILE => "cookie.txt"
  ));

	$output = curl_exec( $ch );
	curl_close( $ch );

	$result = json_decode( $output, true );
	return $result["query"]["tokens"]["logintoken"];
}

// Step 2: POST Request to log in. Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest( $logintoken ) {
	global $endPoint;

	$params2 = [
		"action" => "login",
		"lgname" => "bot_user_name",
		"lgpassword" => "bot_password",
		"lgtoken" => $logintoken,
		"format" => "json"
	];

	$ch = curl_init();

  curl_setopt_array($ch, array(
    CURLOPT_URL => $endPoint, 
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query( $params2 ),
    CURLOPT_COOKIEJAR =>  "cookie.txt",
    CURLOPT_COOKIEFILE => "cookie.txt"
  ));

	$output = curl_exec( $ch );
	curl_close( $ch );

}

// Step 3: GET Request to fetch CSRF token
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
function mergehistorytimestamp( $csrftoken ) {
  global $endPoint;

  $params4 = [
		"action"=>"mergehistory",
    "from"=>"Oldpage",
    "to"=>"Newpage",
    "format"=>"json",
    "timestamp"=>"2015-12-31T04:37:41Z",
    "reason"=>"Reason"
	];
  $url = $endPoint . "?" . http_build_query( $params4 );
  $header = "Content-Type: application/x-www-form-urlencoded";
  $params5 = [
    "token" => $csrftoken
  ];
  
  $ch = curl_init();

  curl_setopt_array($ch, array(
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_POSTFIELDS => http_build_query( $params5 ),
    CURLOPT_HTTPHEADER => array($header)
  ));

  $response = curl_exec($ch);
  $err = curl_error($ch);

  curl_close($ch);

  if ($err) {
    echo "cURL Error #:" . $err;
  } else {
    echo $response;
  }
}
