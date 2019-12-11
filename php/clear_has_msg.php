<?php

/*
    clear_has_msg.php

    MediaWiki API Demos
    Demo of `ClearHasMsg` module: Clear the hasmsg flag for the current user.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "clearhasmsg",
    "format" => "json"
];

$ch = curl_init();

curl_setopt( $ch, CURLOPT_URL, $endPoint );
curl_setopt( $ch, CURLOPT_POST, true );
curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params ) );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

$response = curl_exec($ch);
curl_close($ch);

echo ($response);
