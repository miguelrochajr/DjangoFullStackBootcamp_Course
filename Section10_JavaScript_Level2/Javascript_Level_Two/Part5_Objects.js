// PART 5: JAVASCRIPT OBJECTS

// Objects are hash tables, they store information in a key-value pair.
// They are very similar to dictionaries in Python.

// Unlike an array, a Javascript Object does NOT retain order, instead you access
// the value you want by entering its corresponding key. They can hold a variety of
// data types, including nested Objects.

// Creating an Object:
var carInfo = { make: "Toyota", year: 1990 , model: "Camry" };

// Call values by their key:
carInfo['model'];

// Flexible data types
// Extreme Example:
var mess = { a: "hello", b: ['x','y','z'] , c: {'inside': [ 4 ,5, ["weird"]]}};

// Grabbing the letter z:
mess['b'][2];

// Changing the value that corresponds to a key:
carInfo['year'] = 2006;
//Show
carInfo['year'];

// Could also reference itself:
carInfo['year'] += 1

//show
carInfo['year'];

// Show Entire Object:
// Sometimes differs by browser -
console.dir(carInfo);

// Iterate through object:
for (var key in carInfo) {
  // Remember there is no order!
  console.log(key)
  console.log(carInfo[key])
  console.log("\n")
}

/////////////////////////
/// OBJECT METHODS /////
///////////////////////

// Besides key-value pairs for normal data types, you can add in methods!

// Methods are essentially functions that are built into a javascript object.
// Usually we've called a function and then passed stuff as parameters, now we
// will build this function inside of an object, creating a method for that object.

// For Example:
var carInfo = {
  make: "Toyota",
  year: 1990 ,
  model: "Camry" ,
  carAlert: function(){
    alert("We've got a car here!")
  }
};

// Then you can call it!
carInfo.carAlert()

// But what if you (more realistically) want to actually reference an object's
// key-value pairs. For instance, if we want ot include this in our alert?

// You'll need to use the "this" keyword
var carInfo = {
  make: "Toyota",
  year: 1990 ,
  model: "Camry" ,
  carAlert: function(){
    alert('Your car info is, make: '+this.make+ " year: "+this.year+ " model:"+this.model)
  }
};

// The "this" keyword can be pretty confusing for beginners, and it behaves
// differently in different situations of use-cases. We will dive deeper into it
// later on. For now, think of it as a way to point out what you are trying to reference.
// For instance, if we didn't have this.make in the previous carAlert example,
// Javascript would have been confused, are we referring to a global variable
// called "make"? Or the key called "make", the this keyword trys to help make
// clear that sort of distinction.

// Okay that is it for now on objects! We will touch back on them later on!
