#########################
#### CONTROL FLOW #######
#########################

# In this lecture we will cover Control Flow in Python, basically how to dictate
# our code behaves in whatever manner we want. Let's start with basic comparison
# Operators:

###########################
## COMPARISON OPERATORS ###
###########################

# Greater than
1 > 2
# Less than
1 < 2
# Greater than or Equal to
1 >= 1
# Less than or Equal to
1 <= 4
# Equality
1 == 1
1 == "1"
'hi' == 'bye'
# Inequality
1 != 2

###########################
### LOGICAL OPERATORS #####
###########################

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

##################################
### if,elif, else Statements #####
##################################

# Indentation is extremely important in Python and is basically Python's way of
# getting rid of enclosing brackets like {} we've seen in the past and are common
# with other languages. This adds to Python's readability and is huge part of the
# "Zen of Python". It is also a big reason why its so popular for beginners. Any
# text editor or IDE should be able to auto-indent for you, but always double check
# this if you ever get errors in your code! Code blocks are then noted by a colon (:).

# Now let's show some examples of if, elif, and else statements:

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# If Else - Make sure to line up the else with the if statement to "connect" them

if 1 < 2:
    print('first')
else:
    print('last')

###
###

if 1 > 2:
    print('first')
else:
    print('last')


# To add more conditions (like else if) you just use a single phrase "elif"

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

################################################################################
####################-----------------------------###############################
####################-----------LOOPS-------------###############################
####################-----------------------------###############################
################################################################################

# Time to review loops with Python, such as For Loops and While loops
# Python is unique in that is discards parenthesis and brackets in favor of a
# whitespace system that defines blocks of code through indentation, this forces
# the user to write readable code, which is great for future you looking back at
# your older code later on!

#####################
### FOR LOOPS #######
#####################

# Use For Loops for any sequence of elements. If you try to use a for loop with
# a mapping like a dictionary, it will still work, but it won't loop with any
# order. Let's walk through some examples of how a for loop behaves with the
# various data structures we've learned about!

## For Loop with a list

# Perform an action with each element
seq = [1,2,3,4,5]

for item in seq:
    print(item)


# Perform an action for every element but doesn't actually involve the elements
for item in seq:
    print('Yep')


# You can call the loop variable whatever you want:
for jelly in seq:
    print(jelly+jelly)

## For Loop with a Dictionary
ages = {"Sam":3,"Frank":4,"Dan":29}

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print("\n")

# A list of tuple pairs is a very common format for functions to return data in
# Because it is so common we can use tuple un-packing to deal with this, example:

mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)

#######################
### WHILE LOOPS #######
#######################

# While loops allow us to continually perform and action until a condition
# becomes true. For example:

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

#####################
### OTHER TOPICS ####
#####################

# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point

# Note that its a generator:
range(5)

list(range(5))

for i in range(5):
    print(i)

# Start and ending
range(1,10)

# Third argument for step-size
range(0,10,2)


# List Comprehension
# This technique allows you to quickly create lists with a single line of code.
# You can think of this as deconstructing a for loop with an append(). For Example:

# Starting with:
x = [1,2,3,4]

# We could do this:
out = []
for item in x:
    out.append(item**2)
print(out)


# Written in List Comprehension Form
[item**2 for item in x]

# List Comprehension is a great tool, but remember its not always approriate for
# every situation, don't sacrafice readability for a list Comprehension. It's
# speed is very comparable to the for loop.
