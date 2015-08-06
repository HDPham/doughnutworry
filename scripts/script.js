 // onclick="$('#plainglaze').show()"
 // onclick="$('#chocosprinkle').hide()"

// function ReceivedImage(data){
//   console.log(data);
//   $("#donutimage").attr("src", data.url);
//   $("#frostingimage").attr("src", data.urlf);
// }
function ReceivedDonut(data){
  console.log(data);
  $("#donutimage").attr("src", data.url);
}
function ReceivedFrosting(data){
  console.log(data);
  $("#frostingimage").attr("src", data.urlf);
}
function ReceivedTopping(data){
  console.log(data);
  $("#toppingimage").attr("src", data.urlt);
}


$(document).ready(function() {

  $("#submit").click(function(e){
    e.preventDefault();
    var selected_value = $("#cakeflavor").val()
    $.post("select", {"selected": selected_value}, ReceivedDonut)
    var selected_value2 = $("#frostingflavor").val()
    $.post("select", {"selected2": selected_value2}, ReceivedFrosting)
    var selected_value3 = $("#toppingflavor").val()
    $.post("select", {"selected3": selected_value3}, ReceivedTopping)
    console.log("button clicked");
 });
});

var map;
var service;
var infowindow;



// Handler for the "coordinates" form
function searchCoords() {
  console.log('Address submitted');
  var lat = $('#lat').val();
  var lon = $('#lon').val();
  if(lat === "" || lon === "") {
    console.log("Not valid");
    window.alert("Need a valid set of coordinates!");
    return false;
  }
  else {
    // Maps API takes bad parameters and ignores them, so we are good.
    $('#address').val("");
    console.log("Valid Address");
    // $.post("record_request", {type: "coords", lat: lat, lon: lon});
    map.setCenter({lat: parseFloat(lat), lng: parseFloat(lon)});
    // We don't want to zoom in too much.
    if(map.getZoom() > 13) {
      map.setZoom(13);
    }
    // console.log(map)
    getRequest();
    return true;
  }
}

function createMarker(place, name) {
  console.log(name);
  var marker = new google.maps.Marker({
    map: map,
    position: place.geometry.location
  });
  // var infoWindowOptions = {content: name};
  // var infoWindow = new google.maps.InfoWindow(infoWindowOptions);
  var infoWindow = new google.maps.InfoWindow();
  infoWindow.setContent('<strong>' + name + '</strong>');
  google.maps.event.addListener(
    marker,
    'click',
    function() {infoWindow.open(map, marker);}
  );
}

// When Geocoder is done, it will call this function with the result.
function callback(results, status) {
  if(status == google.maps.places.PlacesServiceStatus.OK) {
    console.log(results);
    for (var i = 0; i < results.length; i++) {
      var place = results[i];
      createMarker(results[i], results[i].name);
    }
  }
}



// Handler for the "address" form.
function searchAddress() {
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
    // $.post("record_request", {type: "address", address: address});

    // Convert an address into precise locations, one or more, and calls the callback function when done.

    getCoordinates(address);
    google.maps.event.addListenerOnce(map, 'bounds_changed', getRequest);
    return true;
  }
}

function getCoordinates(search_address) {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({address: search_address}, function(results, status) {
    var coords_obj = results[0].geometry.location;
    var coordinates = [coords_obj['G'], coords_obj['K']];
    map.setCenter({lat: coordinates[0], lng: coordinates[1]});
  });
}

function getRequest() {
  var request = {
    bounds: map.getBounds(),
    query: 'donuts'
  }
  service.textSearch(request, callback);
}

function initialize(location) {
  var mapOptions = {
    center: new google.maps.LatLng(location.coords.latitude, location.coords.longitude),
    // center: new google.maps.LatLng(39, -90),
    zoom: 13
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  service = new google.maps.places.PlacesService(map);

  google.maps.event.addListenerOnce(map, 'bounds_changed', getRequest);


  // var acOptions = {types: ['establishment']};
  // var autocomplete = new google.maps.places.Autocomplete(document.getElementById('address'),acOptions);
  // autocomplete.bindTo('bounds',map);
  // var infoWindow = new google.maps.InfoWindow();
  // var marker = new google.maps.Marker({map: map});
  //
  // google.maps.event.addListener(autocomplete, 'place_changed', function() {
  //   infoWindow.close();
  //   var place = autocomplete.getPlace();
  //   if(place.geometry.viewport) {
  //     map.fitBounds(place.geometry.viewport);
  //   }
  //   else {
  //     map.setCenter(place.geometry.location);
  //     map.setZoom(17);
  //   }
  //   marker.setPosition(place.geometry.location);
  //   infoWindow.setContent('<div><strong>' + place.name + '</strong><br>');
  //   infoWindow.open(map, marker);
  //   google.maps.event.addListener(marker,'click',function(e){
  //
  //     infoWindow.open(map, marker);
  //   });
  // });
}

// google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(
  function() {
    navigator.geolocation.getCurrentPosition(initialize)
    // $('#address-button').click(function() {
    //   var address = $('#address').val();
    //   if(address === "") {
    //     console.log("Not valid");
    //     window.alert("Need a valid address!")
    //     return false;
    //   }
    //   else {
    //       console.log("Valid Address");
    //       $('#lat').val("");
    //       $('#lon').val("");
    //       $.post("record_request", {type: "address", address: address});
    //       GeotagAddress(address);
    //       return true;
    //   mapOptions = {
    //     center: new google.maps.LatLng(location.coords.latitude, location.coords.longitude),
    //     zoom: 13
    //   }
    // });
    $('#coords-submit').on('click', searchCoords);
    $('#address-submit').on('click', searchAddress);
  }

);



// http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg
// http://www.metalinsider.net/site/wp-content/uploads/2014/06/chocolate-frosted-sprinkles-HI.jpg

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
