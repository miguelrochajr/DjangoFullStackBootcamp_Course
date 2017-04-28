// This is the code we typed into the console

// Try just the dollar sign:
$

// Grab the h1 header:
$('h1');

// Save it to variable:
var x = $('h1');

// You can easily edit the css properties:
x.css("color",'red');
x.css("background","blue");

// Multiple CSS properties at once:
var newCSS = {
  "color":"white",
  "background":"blue",
  "border":"red"
}

x.css(newCSS);

// Grabbing multiple returns an array-like object:
var listItems = $('li');

// Change all items:
listItems.css("color",'red');

// Grab a particular index item:
listItems.eq(0).css('color','blue');

listItems.eq(1).css('color','purple');

// LastItem
listItems.eq(-1).css('background','red');

///////////////////////
/// TEXT and HTML ////
/////////////////////

// Grabbing Text:
$('h1').text()

// Changing Text:
$('h1').text("Brand New Text!")

// Grabbing HTML
$('h1').html()

// Changing HTML
$('h1').html("<em>Now in Italics</em>")

////////////////////////////
// ATTRIBUTES and VALUES //
//////////////////////////

// Changing an attribute
$("input").eq(1).attr('type','checkbox');

// Changing values
$("input").eq(0).attr('value',"BRAND NEW VALUE");

// Can do this more directly:
$("input").eq(0).val("cleared up");


/////////////////
// CLASSES /////
///////////////

// Add a Class
$('h2').addClass("turnRed")

// Remove a Class
$("h2").removeClass("turnRed");

// Toggle the Class on and Off
$("h3").addClass("turnBlue");

$("h3").toggleClass("turnBlue");
