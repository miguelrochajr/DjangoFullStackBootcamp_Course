# s = "GLOBAL VARIABLE!   "
#
# def func():
#     mylocal=10
#     print(locals())
#     print(globals())
#
# func()



# def hello(name="Jose"):
#     return "hello   "+name
#
# print(hello())
#
# mynewgreet = hello #this is assigning it to the function not to the return value
#
# print(mynewgreet())


# def hello(name="miguel"):
#     print("HELLO FUNC HAS BEEN RUN!")
#
#     def greet():
#         return "This string is inside greet"
#     def welcome():
#         return "This is inside WELCOME!"
#
#     # the following will return a function! remmember: withou the () you pass the function!
#     if name == "miguel":
#         return greet
#     else:
#         return welcome
#
# x = hello()
# print(x())

# def hello():
#     return "Hello, Miguel!"
#
# def other(func):
#     print("Hello!")
#     print(func())
#
# other(hello)
# print(other)

# DECORATOR!!

def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXEC FUNC!")
        func()
        print("FUNC HAS BEEN CALLED!")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION NEEDS A DECORATOR!")

#func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
