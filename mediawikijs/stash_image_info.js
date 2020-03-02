/*
	stash_image_info.js

	MediaWiki API Demos
	Demo of `Stashimageinfo` module: Return information for a stashed file.

	MIT License
*/

var params = {
		action: "query",
    	format: "json",
    	prop: "stashimageinfo",
    	siifilekey: "124sd34rsdf567"
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
