# modules and packages
# whenever you create a file, python creates a variable and assign value to it >>> __name__ = "__main__"
# when you import this from from another file, the __name__ is not equal to "__main__"
# this is not important, but used for initializing things
def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
