$('button').on("click",function(){
  $('button').not(this).removeClass();
  $(this).toggleClass('active');

  });
