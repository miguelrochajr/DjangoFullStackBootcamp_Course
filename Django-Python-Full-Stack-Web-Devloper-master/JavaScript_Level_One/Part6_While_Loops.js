// While Loops
//
// while loops are a while to have your program continuously run some block of code
// until a condition is met (made TRUE). The syntax is:
//
// while (condition){
//     # Code executed here
//     # while condition is true
// }
//
// A major concern when working with a while loop is to make sure that at some
// point the condition should become true, otherwise the while loop will go forever!

// Example
var x = 0

while(x < 5){

    console.log("x is currently: "+ x);
    console.log("x is still less than 5, adding 1 to x");

    // add one to x
    x = x+1;

}


// Can also manually break on conditions, which will exit the loop
// Example
var x = 0

while(x < 5){

    console.log("x is currently: "+ x);

    if(x === 3){
      console.log("x is equal to 3, BREAK")
      break;
    }

    console.log("x is still less than 5, adding 1 to x");

    // add one to x
    x = x+1;

}

// QUICK EXERCISE

// Write a while loop that prints out only the even numbers from 1 to 10.
