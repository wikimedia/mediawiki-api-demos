$( document ).ready(function() {
	var x = document.getElementById( "places-list" );
	
	$( ".btn-search" ).click(function() { 
		getLocation(); 
	});

	function getLocation() {
		x.innerHTML = "Searching your location..";

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(fetchPlaces);
		} else { 
			x.innerHTML = "Geolocation is not supported by this browser.";
		}
	}

	function fetchPlaces(position) {
		var data = { 
			"latitude": position.coords.latitude, 
			"longitude": position.coords.longitude
		};

		$.ajax({
			url: "/", //Change this to /toolname/ for deployment in Toolforge
			type: "POST",
			data: JSON.stringify(data),
			contentType: "application/json",
			dataType: "json",

			success: function (response) { 
				var places = response["results"],
					no_thumb = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Gnome-image-missing.svg/200px-Gnome-image-missing.svg.png";

				x.innerHTML = "";
				
				for (var p in places) {
					var thumbnail = places[p].thumbnail || no_thumb;

					x.innerHTML += "<div class=\"item\"><div class=\"col-xs-8 no-padding\"><h5><a href=\"" +
						places[p]["articleUrl"] + "\" target=\"_blank\">" +
						places[p]["title"] + "</a></h5><p>" +
						places[p]["description"] + "</p><span>📍" + places[p]["distance"] +
						" miles</p></div><div class=\"col-xs-4 no-padding\"><img src=\"" +
						thumbnail + " \"></div></div>";
				}
			}, 
			error: function () { x.innerHTML = "An error occured while fetching places!"; }
		});
	}
});
