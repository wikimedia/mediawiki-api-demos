/*
	get_deleted_revisions.js

	MediaWiki API Demos
	Demo of `Deletedrevs` module: List the six most recent deleted revisions from User:Catrope

	MIT License
*/

var params = {
		action: 'query',
		list: 'deletedrevs',
		druser: 'Catrope',
		drprop: 'revid|user|minor|len|token',
		drlimit: '6',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	var pages = data.query.deletedrevs,
		p,
		drev;
	for ( p in pages ) {
		console.log( 'Revision for Page ' + pages[ p ].title );
		for ( drev in pages[ p ].revisions ) {
			console.log( pages[ p ].revisions[ drev ] );
		}
	}
} );
