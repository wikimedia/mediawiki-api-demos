/*
	general_site_info.js

    MediaWiki API Demos
    Demo of `Siteinfo` module: Obtain general site info.

    MIT License
*/

var params = {
    action: "query",
    meta: "siteinfo",
    formatversion: "2",
    format: "json"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );
