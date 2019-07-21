/*
	watch.js

	MediaWiki API Demos
	Demo of `Watch` module: Add a page to your watchlist

	MIT License
*/

var params = {
		action: 'watch',
		titles: 'Sandbox',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'watch', params ).done( function ( data ) {
	console.log( data );
} );
