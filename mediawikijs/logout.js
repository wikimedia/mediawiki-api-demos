/*
	logout.js

	MediaWiki API Demos
	Demo of `Logout` module: Log out and clear session data.

	MIT License
*/

var params = {
		action: 'logout',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
