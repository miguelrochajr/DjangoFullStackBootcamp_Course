// FOR LOOPS

// Javascript has two types of For Loops:
// * for - loops through a block of code a number of times
// * for/in - loops through elements of an object sequence
//
// There is also the for/of loop, which we will discuss when we reach arrays.
//
// Let's take  a look at some examples to clarify the differences between these two

// The For Loop

// A simple for loop is almost another way of re-writing a while loop.
//
// The for loop has the following syntax:
//
// for (statement 1; statement 2; statement 3) {
//     code block to be executed
// }
// Statement 1 is executed before the loop (the code block) starts.
//
// Statement 2 defines the condition for running the loop (the code block).
//
// Statement 3 is executed each time after the loop (the code block) has been executed.

for (i = 0; i < 5; i=i+1) {
    console.log("Number is " + i );
}

// Can be written as i++ (very common)
for (i = 0; i < 5; i++) {
    console.log("Number is " + i );
}


// What do you think will happen here?
var word = "ABCDEFGHIJK"
for (i = 0; i < word.length; i++) {
    console.log(word[i]);
}

// What do you think will happen here?
var word = "ABABABABABA"
for (i = 0; i < word.length; i=i+2) {
    console.log(word[i]);
}
