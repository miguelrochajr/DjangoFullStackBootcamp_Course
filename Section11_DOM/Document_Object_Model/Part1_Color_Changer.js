// Alright so we've discussed the way you can grab html elements, let's
// see how we can interact with them in Javascript!

// Type this into your console:

// Grab the Header with h1
var header = document.querySelector("h1")

// Then you can interface with the object.

// Interface with the style.
//You will see a ton of options show up!
header.style.color = 'red'

// Now let's connect it to the script to
// change it once every second to a random color!

// Random Color Function:

// http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}

// Simple function for clarity
function changeHeaderColor(){
  colorInput = getRandomColor()
  header.style.color = colorInput;
}

// Now perform the action over intervals (milliseocnds):
setInterval("changeHeaderColor()",500);
