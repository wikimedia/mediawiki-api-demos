<?php
/*
    filearchive.php

    MediaWiki API Demos
    Demo of `Filearchive` module: Enumerate all deleted files from filearchive table sequentially.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action"=> "query",
    "format"=> "json",
    "list" =>"filearchive"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

$result = json_decode( $output, true );
print_r($output);

foreach( $result["query"]["filearchive"] as $k => $v ) {
    echo( $v["name"] . "\n" );
}
