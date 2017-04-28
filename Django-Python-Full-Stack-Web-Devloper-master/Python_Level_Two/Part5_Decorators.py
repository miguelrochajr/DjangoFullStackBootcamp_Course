###################
### Decorators ####
###################
#
# Decorators can be thought of as functions which modify the "functionality" of
# another function. They help to make your code shorter and more "Pythonic".
# They are also used a lot in Python Web Frameworks, which is why we need to learn
# them.

# To properly explain decorators we will slowly build up from functions.
# So lets break down the steps:
#
###################
# Functions Review
###################

def func():
    return 1

func()

###################
# Scope Review
###################

# Remember from the nested statements lecture that Python uses Scope to know what
# a label is referring to.
# For example:

s = 'Global Variable'

def func():
    print(locals())


# Remember that Python functions create a new scope, meaning the function has
# its own namespace to find variable names when they are mentioned within the
# function. We can check for local variables and global variables with the local()
# and globals() functions.

# For example:
print(globals())


# Here we get back a dictionary of all the global variables, many of them are
# predefined in Python. So let's go ahead and look at the keys:

print(globals().keys())


# Note how "s" is there, the Global Variable we defined as a string:

globals()['s']


# Now lets run our function to check for any local variables in the func()
# (there shouldn't be any)
func()


# Great! Now lets continue with building out the logic of what a decorator is.
# Remember that in Python everything is an object! That means functions are
# objects which can be assigned labels and passed into other functions. Lets
# start with some simple examples:

def hello(name='Jose'):
    return 'Hello '+name

hello()


# Assign a label to the function.  Note that e are not using parentheses here
# because we are not calling the function hello, instead we are just putting
# it into the greet variable.

greet = hello

greet
# Call it
greet()


# This assignment is not attached to the original function:

del hello

hello()

greet()

######################################
# Functions within functions
######################################

# Great! So we've seen how we can treat functions as objects, now lets see how
# we can define functions inside of other functions:

def hello(name='Jose'):
    print 'The hello() function has been executed'

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()
# Uh oh!
welcome()


# Note how due to scope, the welcome() function is not defined outside of the
# hello() function. Now lets learn about returning functions from within functions:

######################################
# Returning Functions
######################################

def hello(name='Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()


# Now lets see what function is returned if we set x = hello(), note how the
# closed parenthesis means that name has been defined as Jose.
x

# Great! Now we can see how x is pointing to the greet function inside of the
# hello function.
print(x())


# Lets take a quick look at the code again.
#
# In the if/else clause we are returning greet and welcome, not greet() and welcome().
#
# This is because when you put a pair of parentheses after it, the function
# gets executed; whereas if you don’t put parenthesis after it, then it can be
# passed around and can be assigned to other variables without executing it.
#
# When we write x = hello(), hello() gets executed and because the name is Jose
# by default, the function greet is returned. If we change the statement to
# x = hello(name = "Sam") then the welcome function will be returned. We can
# also do print hello()() which outputs now you are in the greet() function.

######################################
# Functions as Arguments
######################################

# Now lets see how we can pass functions as arguments into other functions:

def hello():
    return 'Hi Jose!'

def other(func):
    print 'Other code would go here'
    print func()

other(hello)


# Great! Note how we can pass the functions as objects and then use them within
# other functions. Now we can get started with writing our first decorator:

######################################
# Creating a Decorator
######################################

# In the previous example we actually manually created a Decorator. Here we will
# modify it to make its use case clear:

def new_decorator(func):

    def wrap_func():
        print "Code would be here, before executing the func"

        func()

        print "Code here will execute after the func()"

    return wrap_func

def func_needs_decorator():
    print "This function is in need of a Decorator"

func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()


# So what just happened here? A decorator simple wrapped the function and
# modified its behavior. Now lets understand how we can rewrite this code using
# the @ symbol, which is what Python uses for Decorators:

@new_decorator
def func_needs_decorator():
    print "This function is in need of a Decorator"

func_needs_decorator()


# Great! You've now built a Decorator manually and then saw how we can use
# the @ symbol in Python to automate this and clean our code. You'll run into
# Decorators a lot if you begin using Python for Web Development, such as Django!
