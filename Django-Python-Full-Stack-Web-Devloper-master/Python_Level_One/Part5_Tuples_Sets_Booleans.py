##################################
## Tuples, Sets, and Booleans ####
##################################
#
# In Python tuples are very similar to lists, however, unlike lists they are
# immutable meaning they can not be changed. You would use tuples to present
# things that shouldn't be changed, such as days of the week, or dates on a calendar.
#
# In this section, we will get a brief overview of the following:
#
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples.
#
# You'll have an intuition of how to use tuples based on what you've learned
# about lists. We can treat them very similarly with the major distinction being
# that tuples are immutable.
#
############################
#### Constructing Tuples ###
############################
#
# The construction of a tuples use () with elements separated by commas. For example:

# Can create a tuple with mixed types
t = (1,2,3)

# Check len just like a list
len(t)

# Can also mix object types
t = ('one',2)

# Show
t

# Use indexing just like we did in lists
t[0]

# Slicing just like a list
t[-1]

############################
### Basic Tuple Methods ####
############################

# Tuples have built-in methods, but not as many as lists do.
# Lets look at two of them:

# Use .index to enter a value and return the index
t.index('one')

# Use .count to count the number of times a value appears
t.count('one')

####################
### Immutability ###
####################

# It can't be stressed enough that tuples are immutable.
# To drive that point home:

t[0]= 'change'

# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

t.append('nope')

############################
### When to use Tuples #####
############################

# You may be wondering, "Why bother using tuples when they have fewer available
# methods?" To be honest, tuples are not used as often as lists in programming,
# but are used when immutability is necessary. If in your program you are passing
#  around an object and need to make sure it does not get changed, then tuple
# become your solution. It provides a convenient source of data integrity.
#
# You should now be able to create and use tuples in your programming as well as
# have an understanding of their immutability.
#

########################################################
########################################################
############## SETS AND BOOLEANS #######################
########################################################
########################################################
#
# There are two other object types in Python that we should quickly cover. Sets and Booleans.
#
############
### Sets ###
############

# Sets are an unordered collection of *unique* elements. We can construct them
# by using the set() function. Let's go ahead and make a set to see how it works

x = set()

# We add to sets with the add() method
x.add(1)

#Show
x


# Note the curly brackets. This does not indicate a dictionary! Although you can
# draw analogies as a set being a dictionary with only keys.
#
# We know that a set has only unique entries. So what happens when we try to add
# something that is already in a set?

# Add a different element
x.add(2)

#Show
x

# Try to add the same element
x.add(1)

#Show
x


# Notice how it won't place another 1 there. That's because a set is only
# concerned with unique elements! We can cast a list with multiple repeat
# elements to a set to get the unique elements. For example:

# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(l)

##########################
######## Booleans ########
##########################
# Python comes with Booleans (with predefined True and False displays that are
# basically just the integers 1 and 0). It also has a placeholder object called
# None. Let's walk through a few quick examples of Booleans (we will dive
# deeper into them later in this course).

# Set object to be a boolean
a = True

#Show
a


# We can also use comparison operators to create booleans. We will go over all
# the comparison operators later on in the course.

# Output is boolean
1 > 2


# We can use None as a placeholder for an object that we don't want to reassign yet:

# None placeholder
b = None


# Thats it! You should now have a basic understanding of Python objects and
# data structure types. Next, go ahead and do the Review Exercises!
