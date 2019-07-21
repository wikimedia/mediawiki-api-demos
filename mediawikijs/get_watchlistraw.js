/*
	get_watchlistraw.js

	MediaWiki API Demos
	Demo of `Watchlistraw` module: Get three pages on the logged-in user's
    watchlist from the main namespace.

	MIT License
*/

var params = {
		action: 'query',
		list: 'watchlistraw',
		wrnamespace: '0',
		wrlimit: '3',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );
