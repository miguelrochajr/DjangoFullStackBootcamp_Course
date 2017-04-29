//Restart the Game

var restart = document.querySelector("#button_restart")

//Grab all the table cells
var squares = document.querySelectorAll("td");

//Clear all cells
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}

restart.addEventListener("click", clearBoard);


function changeCell(){
  if(this.textContent === ''){
    this.textContent = 'X';
  } else if(this.textContent === 'X'){
    this.textContent === 'O';
  } else {
    this.textContent === '';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", changeCell);
}
