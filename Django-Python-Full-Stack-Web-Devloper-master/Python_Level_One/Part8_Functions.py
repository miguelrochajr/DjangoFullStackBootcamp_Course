######################
####--FUNCTIONS--#####
######################

# This lecture will consist of explaining what a function is in Python and how to
# create one. Functions will be one of our main building blocks when we construct
# larger and larger amounts of code to solve problems.
#
# So what is a function?
#
# Formally, a function is a useful device that groups together a set of statements
# so they can be run more than once. They can also let us specify parameters that
# can serve as inputs to the functions.
#
# On a more fundamental level, functions allow us to not have to repeatedly write
# the same code again and again. If you remember back to the lessons on strings and
# lists, remember that we used a function len() to get the length of a string.
# Since checking the length of a sequence is a common task you would want to write
# a function that can do this repeatedly at command.
#
# Functions will be one of most basic levels of reusing code in Python, and it will
# also allow us to start thinking of program design (we will dive much deeper
# into the ideas of design when we learn about Object Oriented Programming).
#

######################
# def Statements
######################

# Let's see how to build out a function's syntax in Python.
# It has the following form:

def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)

# We begin with def then a space followed by the name of the function. Try to keep
# names relevant, for example len() is a good name for a length() function. Also
# be careful with names, you wouldn't want to call a function the same name as a
# built-in function in Python (such as len).
#
# Next come a pair of parenthesis with a number of arguments separated by a comma.
# These arguments are the inputs for your function. You'll be able to use these
# inputs in your function and reference them. After this you put a colon.
#
# Now here is the important step, you must indent to begin the code inside your
# function correctly. Python makes use of whitespace to organize code. Lots of
# other programing languages do not do this, so keep that in mind.
#
# Next you'll see the doc-string, this is where you write a basic description of
# the function. Using iPython and iPython Notebooks, you'll be ab;e to read these
# doc-strings by pressing Shift+Tab after a function name. Doc strings are not
# necessary for simple functions, but its good practice to put them in so you or
# other people can easily understand the code you write.
#
# After all this you begin writing the code you wish to execute.
# The best way to learn functions is by going through examples.
# So let's try to go through examples that relate back to the various objects
# and data structures we learned about before.
#
# ######################
# Example 1
# ######################

# A simple print 'hello' function

def hello():
    print("hello")

hello()

# ######################
# Example 2
# ######################

# We can expand on this by using the return keyword, that way we can actually return
# a result and save it for future use, instead of just displaying it. Notice the
# lack of parenthesis or brackets, this is the power of whitespace!

def giveMeHello():
    return "hello"

result = giveMeHello()
print(result)

# Common mistake:
print(giveMeHello)

# ######################
# Example 3
# ######################
#
# Let's write a function that returns tells you whether a number is even or not

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))

    # Experienced way: (Don't need an if statement)
    print(num%2 == 0)

evenCheck(41)

# ######################
# Example 4
# ######################
#
# Let's write a function that will greet you!
#

def helloYou(name="Default Name"):
    return("Hello, "+name)

# Try this with and without a name
result = helloYou()
print(result)

# ######################
# Example 5
# ######################
#
# Let's write a function that will add two numbers together, only if they are even!
#

def addEvenOnly(num1,num2):
    """
    INPUT: Two numbers
    OUTPUT: False if both numbers are not even,
    the sum if both numbers ar even
    """
    if (num1 % 2!=0) or (num2 % 2 != 0):
        return False
    else:
        return num1+num2

x = addEvenOnly(1,2)
y = addEvenOnly(2,2)
print(x)
print(y)

# ######################
# Lambda Expressions
# ######################

#  You won't always need a full blown function, often you will just want to use
#  a function only once, in some of these cases, it makes more sense to use a
# lambda expression, also known as an anonymous function. Let's see an example:

def timesTwo(num):
    return num*2

# Lambda expression
lambda num: num*2

# To really understand the use case for this, we need to introduce a function
# that accepts other functions as input parameters, in this case, we will use filter:
#
my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2 == 0

evens = filter(evenBool,my_list)
print(list(evens))

# Now with Lambda!
evens = filter(lambda num: num%2==0,my_list)
print(list(evens))

# Alright, you should now be ready for your exercises! Some exercise questions
# may be easier with knowledge of methods, we've seen this a bit before, but here
# is an optional review!

# ######################
# Methods
# ######################

# Methods are almost like functions that are built into the object. Some Methods
# return something, others just affect the object in place. Later on in the OOP
# section we will learn how to create our own methods. For now, here are some
# useful common ones (this may be review)

st = 'hello my name is Sam'
st.lower()
st.upper()
st.split()

tweet = 'Go Sports! #Sports'
tweet.split('#')
tweet.split('#')[1]

d = {'k1':1,'k2':2}
d.keys()
d.items()

lst = [1,2,3]
x = lst.pop()

# in Operator (not a method, just something useful)
'x' in [1,2,3]
'x' in ['x','y','z']
