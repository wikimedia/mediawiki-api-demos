/*
	userrights.js

	MediaWiki API Demos
	Demo of `Userrights` module: Add and remove user rights by
    changing the user's group membership.

	MIT License
*/

var params = {
		action: 'userrights',
		user: 'ABCD',
		add: 'sysop',
		reason: 'Added ABCD to the sysop group',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'userrights', params ).done( function ( data ) {
	console.log( data );
} );
