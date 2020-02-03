/*
	user_info.js

	MediaWiki API Demos
	Demo of `Userinfo` module: Get general user info and user rights.

	MIT License
*/

var params = {
		action: 'query',
		meta: 'userinfo',
		uiprop: 'rights',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
