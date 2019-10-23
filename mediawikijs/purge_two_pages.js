/*  
    purge_two_pages.js
 
    MediaWiki API Demos
    Demo of `purge` module: Sending post request to purge two or more pages

    MIT license
*/

var params = {
		action: 'purge',
		titles: 'Main_Page|Nonexistent',
		format: 'json'
	},
	api = new mw.Api();

api.post( params ).done( function ( data ) {
	console.log( data );
} );
