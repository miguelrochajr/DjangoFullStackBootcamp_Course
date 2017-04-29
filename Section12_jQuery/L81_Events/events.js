/*
$('h1').click( function(){
  $(this).text("CHANGED")
})

$('li').click(function(){
  console.log("Any li was clicked!");
})
*/

//KEY PRESS

// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue');
// })

$('input').eq(0).keypress(function(event){
  if(event.which === 13){
    $('h3').toggleClass('turnBlue');
  }
})

//on method
$('h1').on('mouseenter', function(){
  $(this).toggleClass('turnBlue');
})

//events and ANIMATIONS
$("input").eq(1).on("click", function(){
  $('.container').slideUp(3000);
})
