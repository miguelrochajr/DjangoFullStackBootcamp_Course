// FUNCTIONS

// Functions will be one of our main building blocks when we construct
// larger and larger amounts of code to solve problems.
//
// So what is a function?
//
// Formally, a function is a useful device that groups together a set of statements
// so they can be run more than once. They can also let us specify parameters that
// can serve as inputs to the functions.
// On a more fundamental level, functions allow us to not have to repeatedly write
// the same code again and again.

// Functions are one of the most critical parts of being able to use JavaScript
// effectively, so once you are done learning how to create them you will have
// an extensive exercise testing your ability to use them to solve problems!

// In JavaScript, functions follow this general form:
// (parameters are also commonly called arguments)

function name(parameter1, parameter2, parameter3) {
    //code to be executed
}

// Now let's see several examples!

// EXAMPLE
// Simple function with no input parameters
function hello(){
    console.log("hello world!");
}

// This will just return the function:
hello

// You need to add parenthesis (and any parameters you want) to actually call
// the function into action!
hello()


// EXAMPLE
function helloYou(name){
    console.log("hello "+name);
}
helloYou("Jose")

// EXAMPLE
function addNum(num1,num2){
    console.log(num1+num2);
}
addNum(30,20)

/////////////////////
// Default values //
///////////////////


//
// Notice that so far we've had to define every single argument in the function
// when using it, but we can also have default values by using an equals sign,
// for example:

// EXAMPLE
function helloSomeone(name="Frankie"){
    console.log("Hello "+name);
}

helloSomeone()
///////////////////////
// Returning Values //
/////////////////////

// So far we've only been printing out results, but what if we wanted to return
// the results so that we could assign them to a variable, we can use the return
// keyword for this task in the following manner:

// EXAMPLE

// Without Return
function formal(name="Sam",title="Sir"){
    console.log(title+" "+name)
}

//
"Welcome " + formal()
// Welcome undefined


// With a return
function formal(name="Sam",title="Sir"){
    return title+" "+name;
}

//
"Welcome "+formal()
//

var result = formal()

////////////////////
// SCOPE //////////
//////////////////

// Scope is the term we use to describe how objects and variable get defined
// within JavaScript. When discussing scope with functions, as a general rule we
// can say that if a variable is defined only inside a function than its scope is
// limited to that function. For example, consider the following function:

// EXAMPLE

// Multiplies input by 5
function times5(numInput) {
  var result = numInput * 5
  return result
}

times5(5)

// Now after running the function try calling:
numInput // Error
result // Error

// Not defined outside the scope of the function!

// These errors indicate that these variables are only defined inside the scope of
// the function. So variables defined inside of a function are only defined
// (or redefined) inside of that function. However, variables assigned outside of
// the function are global variables, and the function will have access to them
// due to their scope. For example:

var v = "I'm global v"
var stuff = "I'm global stuff"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff inside func";
    console.log(stuff);
}

// Now see what happens!
fun()

// So what is happening above? The following happens
// console.log(v); will check for the global variable v, the outer scope
// console.log(stuff); will also check for the global variable stuff
// fun(stuff) will accept an argument stuff, print out v, and then reassign stuff
// (in the scope of the function) and print out stuff.
//
// Notice two things:
//
// The reassignment of stuff only effects the scope
// of the stuff variable inside the function
//
// The fun function first checks to see if v is defined
// at the function scope, if not (which was the case) it
// will then search the global scope for a variable names v,
// leading to it printing out "I'm global v".

// Okay! Now you are ready to tackle some actual exercise problems!
