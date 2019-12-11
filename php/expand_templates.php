<?php

/*
    expand_templates.php

    MediaWiki API Demos
    Demo of `Expandtemplates` module: Expand the Project:Sandbox template.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "expandtemplates",
    "text" => "{{Project:Sandbox}}",
    "prop" => "wikitext",
    "format" => "json"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

echo( $output );
