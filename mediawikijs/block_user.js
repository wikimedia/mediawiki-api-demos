/*
	block_user.js

	MediaWiki API Demos
	Demo of `Block` module: sending POST request to block user

	MIT License
*/

var params = {
		action: 'block',
		user: 'ABCD',
		expiry: '2020-02-25T07:27:50Z',
		reason: 'API Test',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
