// var player1 = prompt("Player One: Enter Your Name , you will be Blue");
// var player1Color = 'rgb(86, 151, 255)';
//
// var player2 = prompt("Player Two: Enter Your Name, you will be Red");
// var player2Color = 'rgb(237, 45, 73)';


$('td').click(function(){
  $(this).find('button').css("background", "blue");
})
