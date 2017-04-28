// Start off with basic console commands
// We will be running all of these in the Google Chrome Console to start off.

// Show a prompt
alert("Hello World.")

////////////////////////
// Basic Data Types ///
//////////////////////

// Numbers (same for integers, floats, negatives)
10
10.5
-10

// Strings - Wrapped in Single or Double Quotes
"Hello World."
"10" // Note how this is no longer a number!

// Booleans (logical values)
true
false

// undefined and null
undefined
null


//////////////////////
/// NUMBERS /////////
////////////////////

// Let's use Javascript as a basic calculator

// Addition
2 + 2

// Subtraction
5 - 1

// Multiplication
3 * 2

// Division
10 / 2
2/5

// Exponents
2 ** 4

// Modulo (returns the remainder)
15 % 14
6 % 2
6 % 4


//////////////////////
/// STRINGS /////////
////////////////////

// Strings are sequences of characters
// Each element/character has an indexed position

"django is cool"
'Django is cool'

// Concatentation
"Django" + " is cool"

// Length Attributes
"Django".length
"four four".length

// Escape characters
"hello \n start a new line"
"hello \t give me a tab"
"hello \"quotes\" "

// Index individual characters/elements (starts at zero)
"hello"[0]
"hello"[4]

////////////////////
// VARIABLES //////
//////////////////

// General Form
// var varName = value;

// Let's see some examples
var bankAccount = 100;
var deposit = 50;
var total = account + deposit;

var greeting = "Welcome back: ";
var name = "Jose";
alert(greeting+name)

// undefined (created but not defined)
var myvariable

// null ("nothing" that you set)
var bonus = null

/////////////////////////////////
/// Basic Javascript Methods ///
///////////////////////////////

// Alert Pop-up
alert("hello world")

// Output to console
console.log("Hello world")

// Accept Prompt Inputs
var age = prompt("How old are you?")
