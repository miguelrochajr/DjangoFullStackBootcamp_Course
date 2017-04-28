// Welcome to Part 4 of Javascript Level One!
// It's time to learn how to add some logical capabilities to our JS code.
// You can type these commands into the browser console

// Let's review booleans
true
false

////////////////////////////
// Comparison Operators ///
//////////////////////////

// Compare two items and return a boolean
// Pay special attention when we reach equality!


// Greater Than
3 > 2;
2 > 3;

// Less Than
1 < 2;

// Greater than or equal to
2 >= 2;

// Less than or equal to
1 <= 3;

// Let's now discuss equality and it's quirks in Javascript!

// Equality
2 == 2;
"username" == "username";

// Inequality
2 != 3;

// Hold on a second! What happens with this...
"2" == 2;

// It returned True! Although this may cause errors for some programs!

// JS uses type coercion! This means it will try it's best to convert objects
// to similar data types to perform the comparison! A lot of times you don't
// actually want that!

// We want a way to check equality of both value AND type!
// Add another set of equals signs to do this!

// Check equality of value and type
5 === 5;
5 === "5";

// Check for Inequality of value and type
5 !== "5";
5 !== 5;


/// Okay, now let's talk about a few more situations!
// It's common int programming languages for 0 and 1 to be substitutes for
// true and false.
true == 1;
true === 1;

false == 0;
false === 0;

// Weird behaviour for null, undefined, and NaN values!

null == undefined; // true

NaN == NaN; // false


//////////////////////////
// LOGICAL OPERATORS ////
////////////////////////

// Logical Operators allow us to combine multiple comparison Operators!

// AND is written with &&
// Need both conditions to be true to return true
1 === 1 && 2 ===2;

// OR is written with ||
// Need only one condition to be true to return true
1 === 2 || 1 ===1;

// NOT is written with !
// Basically a way of checking the opposite of a condition
!(1===1);
// Can also stack these (not super common)
!!(1===1);

////////////////////////////////
/// OPTIONAL EXERCISES ////////
//////////////////////////////
// Here are a quick 5 exercise questions for you!
// Mentally evaluate the following expressions, then use the console to check!

var x = 1
var y = 2

// Exercise 1
"2" == y && x === 1;

// Exercise 2
x >= 0 || y === "2";

// Exercise 3
!(x !== 1) && y === (1+1);

// Exercise 4
y !== "2" && x < 10 ;

// Exercise 5
y !== x || y == "2" || x === 3;
