// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks
function display(){
  console.log(roster);
}

function addNew(str){
  roster.push(str);
  console.log(roster);
}

function removeStudent(str){
  var index = roster.indexOf(str);
  if(index == -1){
    alert("Sorry! The name you typed does not exist in our database");
  } else {
    roster.splice(index, 1); // Syntax: array.splice(start, deleteCount). Source: https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/splice?v=example
  }
}


var launchPrompt = prompt ("Would you like to use the roster website prompt? y/n");
var action = "Initial";

while (launchPrompt == 'y'){
  switch(action){
    case "Initial":
      action = prompt("Please select one of the commands: \n add, remove, display or quit ");
      break;
    case "display":
      display();
      action = "Initial";
      break;
    case "add":
      var student = prompt("Please type the name of the one you wish to add:");
      addNew(student);
      action = "Initial";
      break;
    case "quit":
      launchPrompt = false;
      break;
    case "remove":
      var student = prompt("Please type the name of the student you wish to remove:");
      removeStudent(student);
      action = "Initial";
      break;
    default:
      alert("Invalid command. Please choose: \n add, remove, display or quit");
      action = "Initial";
      break;
  }
}

alert("Thank You for using our Web App! \n See you in the next one!");


// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
