/*
	get_deleted_revs.js

	MediaWiki API Demos
	Demo of `Deleted revisions:Get a list of deleted revision for Talk:Main Page` module

	MIT License
*/

var api = new mw.Api();

api.login( 'your_bot_username', 'your_bot_password' ).done( function ( data ) {
	console.log( 'You are logged in as ' + data.login.lgusername );
} );


var params = {
		action: "query",
    	format: "json",
    	titles: "Talk:MainPage",
    	prop:   "deletedrevisions",
    	drv:    "prop"
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	console.log( data );
} );