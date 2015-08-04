 // onclick="$('#plainglaze').show()"
 // onclick="$('#chocosprinkle').hide()"

function ReceivedImage(data){
  console.log(data);
  $("#donutimage").attr("src", data.url);
 $("#plainglaze").fadeIn(1000);
}

$(document).ready(function() {

  $("#submit").click(function(e){
    e.preventDefault();
    var selected_value = $("#cakeflavor").val()
    $.post("select", {"selected": selected_value}, ReceivedImage)
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
