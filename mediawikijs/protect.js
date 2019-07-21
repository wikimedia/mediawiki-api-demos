/*
	protect.js

	MediaWiki API Demos
	Demo of `Protect` module: Demo to change the edit protection
    level of a given page.

	MIT License
*/

var params = {
		action: 'protect',
		title: 'Sandbo2',
		protections: 'edit=autoconfirmed|move=sysop',
		expiry: 'infinite',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
