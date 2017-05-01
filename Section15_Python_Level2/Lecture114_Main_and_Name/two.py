import one

print("Top level  TWO.PY")
one.func()

def myName():
    print(__name__)


if __name__ == '__main__':
    print("two.py being run directly")
else:
    print("two is being imported")
