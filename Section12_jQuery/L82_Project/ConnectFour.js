//The following was made by Jose Padilla with comments and modifications by Miguel Rocha Jr.

var player1 = prompt("Player One: Enter Your Name , you will be Blue");
var player1Color = 'rgb(86, 151, 255)'; //this RGB for a light  Blue
//the jQuery expercts a string in a rgb form to change the colors with these spaces

var player2 = prompt("Player Two: Enter Your Name, you will be Red");
var player2Color = 'rgb(237, 45, 73)';

var game_on = true; //wether the game is on or not
var table = $('table tr'); //


// http://stackoverflow.com/questions/6139407/getting-td-by-index-with-jquery
function reportWin(rowNum,colNum) {
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);
}

function changeColor(rowIndex, colIndex, color){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex, color){
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

//the following function will return the next available button to be painted.
//if the functions finds a gray button, it will return it.
function checkBottom(colIndex){
  var = colorReport = returnColor(5, colIndex);
  for (var row = 5; row>-1; row--) {
    colorReport = returnColor(row,colIndex);
    if(colorReport === 'rgb(128, 128, 128)'){
      return row;
    }
  }
}

function colorMatchCheck(one,two,three,four){
  return (one===two && one===three && one===four one!=='rgb(128, 128, 128)' && one !===undefined);
}

// Check for Horizontal Wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row,col+1) ,returnColor(row,col+2), returnColor(row,col+3))) {
        console.log('horiz');
        reportWin(row,col);
        return true;
      }else {
        continue; //just tells the code to continue and not do anything
      }
    }
  }
}

// Check for Vertical Wins
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col) ,returnColor(row+2,col), returnColor(row+3,col))) {
        console.log('vertical');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1) ,returnColor(row+2,col+2), returnColor(row+3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Game End
function gameEnd(winningPlayer) {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 7; row++) {
      $('h3').fadeOut('fast');
      $('h2').fadeOut('fast');
      $('h1').text(winningPlayer+" has won! Refresh your browser to play again!").css("fontSize", "50px")
    }
  }
}


//Strting with the player number 1
var currentPlayer =1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(player1+": it is your turn, please pick a column to drop your blue chip.");

$('.board button').on('click', function(){

  // Recognize what column was chosen
  var col = $(this).closest("td").index();

  // Get back bottom available row to change
  var bottomAvail = checkBottom(col);

  changeColor(bottomAvail, col, currentColor);

  if(horizontalWinCheck || verticalWinCheck || diagonalWinCheck){
    $('h1').text(currentName + " You have won! Congratulations!");
    $('h3').fadeOut('fast');
    $('h2').fadeOut('fast');
  }

  currentPlayer = currentPlayer*-1;

  if(currentPlayer === 1){
    currentName = player1;
    $('h3').text(currentName+ " it is your turn.");
    currentColor = player2Color;
  }else{
    currentName = player2;
    $('h3').text(currentName+ " it is your turn.");
    currentColor = player2Color;
  }

})


// $('td').click(function(){
//   $(this).find('button').css("background", "blue");
// })





// --- THE FOLLOWING CODES WERE TAKEN FROM THE INSTRUCTOR NOTES BUT I ADDED SOME IMPORTANT COMMENTS

//Check out the documentation about the closest():
//http://api.jquery.com/closest/

// $('.board button').on('click',function(){
//   // This is the Column Number (starts at zero):
//   console.log('This is the Column:');
//   console.log($(this).closest("td").index()); //closest(selector) looks for the colosest element on the DOM tree matchin the tag 'selector'. It begins with itself.
//   // This is the Row Number:
//   console.log("This is the Row:");
//   console.log($(this).closest("tr").index());
//   console.log('\n');
//   // This is a way to grab a particular cell (replace):
//   // $('table').eq(rowIndex).find('td').eq(colIndex)
// });
