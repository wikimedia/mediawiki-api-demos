/*
	move.js

	MediaWiki API Demos
	Demo of `Move` module: Move a page with its talk page,
	leaving a redirect behind.

	MIT License
*/

var params = {
		action: 'move',
		from: 'Current title',
		to: 'Page with new title',
		reason: 'API Test',
		movetalk: '1',
		noredirect: '1',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
