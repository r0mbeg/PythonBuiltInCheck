import sys

class Vehicle():
    def __init__(self):
        pass

def foo():
    #tests:
    a = 1
    b = [1, 3, 2]
    c = [[1, 3], 5]
    d = "str"
    v = Vehicle()
    print_vars()

def print_vars():
    dictionary = sys._getframe(1).f_locals
    for key, value in dictionary.items():
        # In Python3 the module is called __builtins__
        # In Python3.7 the module is called builtins
        if (value.__class__.__module__ == 'builtins'):
            print(key, ": True")
        else:
            print(key, ": False")

foo()

