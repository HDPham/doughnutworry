 // onclick="$('#plainglaze').show()"
 // onclick="$('#chocosprinkle').hide()"

function ReceivedImage(data){
  console.log(data);
  $("#donutimage").attr("src","http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg");
 $("#plainglaze").fadeIn(1000);
}

$(document).ready(function() {

  $("#submit").click(function(e){
    e.preventDefault();
    $.post("SelectDonutHandler", {"selected":"plain"}, ReceivedImage)
    console.log("button clicked");
 });
});

// http://dennisdanvers.com/wp-content/uploads/2014/08/donut.jpg
// http://www.metalinsider.net/site/wp-content/uploads/2014/06/chocolate-frosted-sprinkles-HI.jpg

// select handler
