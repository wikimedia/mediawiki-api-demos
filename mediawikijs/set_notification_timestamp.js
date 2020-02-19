/*
	set_notification_timestamp.js

    MediaWiki API Demos
    Demo of `Setnotificationtimestamp` module: Reset the notification status for the entire watchlist.

    MIT license
*/

var params = {
    action: 'setnotificationtimestamp',
    entirewatchlist: '',
    format: 'json'
},
api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
console.log( data );
} );