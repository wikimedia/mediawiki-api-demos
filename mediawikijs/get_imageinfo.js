// This file is autogenerated. See modules.json and autogenerator.py for details

/*
	get_imageinfo.js

	MediaWiki API Demos
	Demo of `Imageinfo` module: Get information about an image file.

	MIT License
*/

var params = {
		action: 'query',
		format: 'json',
		prop: 'imageinfo',
		titles: 'File:Billy Tipton.jpg'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	var pages = data.query.pages,
		p;
	for ( p in pages ) {
		console.log( pages[ p ].title + ' is uploaded by User:' + pages[ p ].imageinfo[ 0 ].user );
	}
} );
