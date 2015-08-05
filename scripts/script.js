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
