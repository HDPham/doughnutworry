 // onclick="$('#plainglaze').show()"
 // onclick="$('#chocosprinkle').hide()"

function ReceivedImage(data){
  console.log(data);
  $("#donutimage").attr("src", data);
 $("#plainglaze").fadeIn(1000);
}

$(document).ready(function() {

  $("#submit").click(function(e){
    e.preventDefault();
    $.post("select", {"selected":"plain"}, ReceivedImage)
    console.log("button clicked");
 });
});


//Stores a list of the markers currently displayed
markers = [];

// Sets the center location of the map
function SetCenter(center) {
  map.setCenter(center);
}

// Removes all existing markers from the map
function ClearMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);  // Remove from map
  }
  markers = [];  // Empty the array
}

// Handler for the "coordinates" form
function CenterOnCoords(e) {
  //e.preventDefault();
  ClearMarkers();  // Remove markers if any
  e.preventDefault();
  console.log('Address submitted');
  var lat = $('#lat').val();
  var lon = $('#lon').val();
  if(lat === "" || lon === "") {
    console.log("Not valid");
    window.alert("Need a valid set of coordinates!");
    return false;
  }
  else {
    // Maps API takes bad parameters and ignores them, so we
    // are good.
    $('#address').val("");
    console.log("Valid Address");
    $.post("record_request", {type: "coords", lat: lat, lon: lon});
    SetCenter({lat: parseFloat(lat), lng: parseFloat(lon)});
    // We don't want to zoom in too much.
    if(map.getZoom() > 13) {
      map.setZoom(13);
    }
    return true;
  }
}

// When Geocoder is done, it will call this function with the result.
function GeocoderCallback(results, status) {
  if(status === "OK") {
    console.log("We've got " + results.length + " results");
    var bounds = new google.maps.LatLngBounds();
    for(var i = 0; i < results.length; i++) {
      var location = results[i].geometry.location;
      // Create new marker and place it on the map.
      var marker = new google.maps.Marker({position: location, map: map, title: results[i].formatted_address});
      // Save marker, we will use it later to remove them.
      markers.push(marker);
      // Increase the area to be visualized if necessary.
      bounds.extend(marker.getPosition());
    }
    map.fitBounds(bounds);
    // We don't want to zoom in too much.
    if(map.getZoom() > 13) {
      map.setZoom(13);
    }
  }
}

// Convert an address into precise locations, one or more, and calls the callback
// function when done.
function GeotagAddress(search_address) {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({address: search_address}, GeocoderCallback);
}

// Handler for the "address" form.
function CenterOnAddress(e) {
  ClearMarkers();
  e.preventDefault();
  console.log('Address submitted');
  var address = $('#address').val();
  if(address === "") {
    console.log("Not valid");
    window.alert("Need a valid address!")
    return false;
  }
  else {
    console.log("Valid Address");
    $('#lat').val("");
    $('#lon').val("");
    $.post("record_request", {type: "address", address: address});
    GeotagAddress(address);
    return true;
  }
}

function initialize() {
  var mapOptions = {
    center: {lat: 39, lng: -96},
    zoom: 3
  };
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  // var markerOptions = {
  //   position: {lat: 39, lng: -96}
  // };
  // var marker = new google.maps.Marker(markerOptions);
  // marker.setMap(map);
  // var acOptions = {
  //   types: ['establishment']
  // };
  // var autocomplete = new google.maps.places.autocomplete(document.getElementById('address'));
  // autocomplete.bindTo('bounds', map);
  //
  // google.maps.event.addListener(autocomplete, 'place_changed', function() {
  //   var place = autocomplete.getPlace();
  //   if(place.geometry.viewport) {
  //     map.fitBounds(place.geometry.location);
  //     map.setZoom(17);
  //   }
  //   else {
  //     map.setCenter(place.geometry.location);
  //     map.setZoom(17);
  //   }
  //   mark.setPosition(place.geometry.location);
  // });
}

// google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(
  function() {
    initialize();
    $('#coord-form').on('submit', CenterOnCoords);
    $('#address-form').on('submit', CenterOnAddress);
  }

);



// http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg
// http://www.metalinsider.net/site/wp-content/uploads/2014/06/chocolate-frosted-sprinkles-HI.jpg

// select handler


// var currentDonut;
// function plainDonut() {
//   var donutImage = document.getElementById('myImage');
//   donutImage.src = "http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg";
// }
//
// function chocolateDonut() {
//   var donutImage = document.getElementById('myImage');
//   donutImage.src = "http://www.metalinsider.net/site/wp-content/uploads/2014/06/chocolate-frosted-sprinkles-HI.jpg";
// }
