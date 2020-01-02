/*
	compare.js

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare the current revisions of two different pages

    MIT license
*/

var params = {
    action: "compare",
    format: "json",
    fromtitle: "Template:Unsigned",
    totitle: "Template:UnsignedIP"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );