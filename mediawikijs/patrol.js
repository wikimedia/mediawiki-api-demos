/*
	patrol.js

	MediaWiki API Demos
	Demo of `Patrol` module: Patrol a recent change

	MIT License
*/

var params = {
		action: 'patrol',
		revid: '77',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'patrol', params ).done( function ( data ) {
	console.log( data );
} );
