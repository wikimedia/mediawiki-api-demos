/*
	namespaces_and_aliases_site_info.js

    MediaWiki API Demos
    Demo of `Siteinfo` module: List namespaces and aliases site info.

    MIT License
*/

var params = {
    action: "query",
    meta: "siteinfo",
    siprop: "namespaces|namespacealiases",
    formatversion: "2",
    format: "json"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );
