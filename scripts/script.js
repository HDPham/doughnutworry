 // onclick="$('#plainglaze').show()"
 // onclick="$('#chocosprinkle').hide()"

$(document).ready(function() {
   $('#submit').change(function() {
       $('.flavor').hide();
       $('.' + $(this).val()).show();
   });
});
