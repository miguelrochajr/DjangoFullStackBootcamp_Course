######################################
# #Errors and Exception Handling
######################################
#
# In this lecture we will learn about Errors and Exception Handling in Python.
# You've definitely already encountered errors by this point in the course.
# For example:
print('Hello


# Note how we get a SyntaxError, with the further description that it was an EOL
# (End of Line Error) while scanning the string literal. This is specific enough
# for us to see that we forgot a single quote at the end of the line. Understanding
# these various error types will help you debug your code much faster.
#
# This type of error and description is known as an Exception. Even if a statement
# or expression is syntactically correct, it may cause an error when an attempt is
# made to execute it. Errors detected during execution are called exceptions and
# are not unconditionally fatal.
#
# You can check out the full list of built-in exceptions
# [here](https://docs.python.org/2/library/exceptions.html).
# now lets learn how to handle errors and exceptions in our own code.

###################
# try and except
###################

# The basic terminology and syntax used to handle errors in Python is the try
# and except statements. The code which can cause an exception to occue is put
# in the try block and the handling of the exception is the implemented in the
# except block of code. The syntax form is:
#
#     try:
#        You do your operations here...
#        ...
#     except ExceptionI:
#        If there is ExceptionI, then execute this block.
#     except ExceptionII:
#        If there is ExceptionII, then execute this block.
#        ...
#     else:
#        If there is no exception then execute this block.
#
# We can also just check for any exception with just using except: To get a
# better understanding of all this lets check out an example: We will look at
# some code that opens and writes a file:

try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Now lets see what would happen if we did not have write permission (opening only with 'r'):


try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Great! Notice how we only printed a statement! The code still ran and we were
# able to continue doing actions and running code blocks. This is extremely
# useful when you have to account for possible input errors in your code.
# You can be prepared for the error and keep running code, instead of your code
# just breaking as we saw above.
#
# We could have also just said except: if we weren't sure what exception would occur.
# For example:

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Great! Now we don't actually need to memorize that list of exception types!
# Now what if we kept wanting to run code after the exception occurred? This is
#  where **finally** comes in.

###################
# finally
###################

# The finally: block of code will always be run regardless if there was an
# exception in the try code block. The syntax is:
#
#     try:
#        Code block here
#        ...
#        Due to any exception, this code may be skipped!
#     finally:
#        This code block would always be executed.
#
# For example:

try:
   f = open("testfile", "w")
   f.write("Test write statement")
finally:
   print("Always execute finally code blocks")



# **Great! Now you know how to handle errors and exceptions in Python with the
# try, except, else, and finally notation!**
