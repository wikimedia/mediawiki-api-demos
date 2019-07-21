/*
	upload_file_from_url.js

	MediaWiki API Demos
	Demo of `Upload` module: Post request to upload a file from a URL

	MIT License
*/

var params = {
		action: 'upload',
		filename: 'New_image.jpg',
		url: 'https://farm9.staticflickr.com/8213/8300206113_374c017fc5.jpg',
		ignorewarnings: '1',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
