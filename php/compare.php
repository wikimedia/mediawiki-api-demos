<?php
/*
    compare.php

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare the current revisions of two different pages
    
    MIT license
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "compare",
    "format" => "json",
    "fromtitle" => "Template:Unsigned",
    "totitle" => "Template:UnsignedIP"

];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

echo( $output );