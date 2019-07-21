/*
	get_watchlist.js

	MediaWiki API Demos
	Demo of `Watchlist` module: Get the currently logged-in user's watchlist.

	MIT License
*/

var params = {
		action: 'query',
		list: 'watchlist',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
