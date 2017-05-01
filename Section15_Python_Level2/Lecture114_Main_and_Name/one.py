# import two
def func():
    print("function in one.py")

print("Top level one.py")
print(__name__)

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")
