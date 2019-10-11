<?php 
/*
    contributors.php

    MediaWiki API Demos
    Demo of `Contributors` module: List all logged-in contributors and count of anonymous contributors to a page.


    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "titles" => "MediaWiki",
    "prop" => "contributors",
    "format" => "json"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

$result = json_decode( $output, true );

foreach( $result["query"]["pages"] as $page ){
    echo ( $output );
}