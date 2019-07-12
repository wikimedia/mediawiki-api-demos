<?php

//This file is autogenerated. See modules.json and autogenerator.py for details

/*
    get_categories.php

    MediaWiki API Demos
    Demo of `Categories` module: Get categories associated with a page.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "format" => "json",
    "prop" => "categories",
    "titles" => "Janelle Monáe"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

$result = json_decode( $output, true );

foreach( $result["query"]["pages"] as $k => $v ) {
    foreach( $v["categories"] as $k => $v ) {
        echo( $v["title"] . "\n" );
    }
}
