$( document ).ready( function() {
    $( ".holidays-html a" ).attr( "target", "_blank" );

    $( ".holidays-html a" ).attr( "href", function( i, href ) {
      return "//en.wikipedia.org" + href;
    });
});