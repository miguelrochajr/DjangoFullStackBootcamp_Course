#####################################
#### Numbers and more in Python! ####
#####################################

# In this lecture, we will learn about numbers in Python and how to use them.
#
# We'll learn about the following topics:
#
#     1.) Types of Numbers in Python
#     2.) Basic Arithmetic
#     3.) Differences between Python 2 vs 3 in division
#     4.) Object Assignment in Python

# Types of numbers
#
# Python has various "types" of numbers (numeric literals). We'll mainly focus on
# integers and floating point numbers.
#
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are
#  examples of integers.
# 
# Floating point numbers in Python are notable because they have a decimal point
# in them, or use an exponential (e) to define the number. For example 2.0 and -2.1
# are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is
# also an example of a floating point number in Python.
#
# Throughout this course we will be mainly working with
# integers or simple float number types.


# Now let's start with some basic arithmetic.

# Basic Arithmetic
# Addition
2+1

# Subtraction
2-1

# Multiplication
2*2


# Division
3/2

# Powers
2**3

# Can also do roots this way
4**0.5

# Order of Operations followed in Python
2 + 10 * 10 + 3

# Can use parenthesis to specify orders
(2+10) * (10+3)


## Variable Assignments
#
# Now that we've seen how to use numbers in Python as a calculator let's see how
# we can assign names and create variables.
#
# We use a single equals sign to assign labels to variables.
# You also don't need to specify the keyword var.
# Let's see a few examples of how we can do this.

# Let's create an object called "a" and assign it the number 5
a = 5

# Now if I call a in my Python script, Python will treat it as the number 5.

# Adding the objects
a+a

# What happens on reassignment? Will Python let us write it over?

# Reassignment
a = 10

# Check
a


# Yes! Python allows you to write over assigned variable names. We can also use
# the variables themselves when doing the reassignment. Here is an example of what I mean:

# Check
a

# Use A to redefine A
a = a + a

# Check
a


# The names you use when creating these labels need to follow a few rules:
#
#     1. Names can not start with a number.
#     2. There can be no spaces in the name, use _ instead.
#     3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#     3. It's considered best practice (PEP8) that the names are lowercase.
#
# Using variable names can be a very useful way to keep track of different
# variables in Python. For example:

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# Show my taxes!
my_taxes


# So what have we learned? We learned some of the basics of numbers in Python.
# We also learned how to do arithmetic and use Python as a basic calculator.
# We then wrapped it up with learning about Variable Assignment in Python.
#
# Up next we'll learn about Strings!
