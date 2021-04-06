def print_vars():
    dict = sys._getframe(1).f_locals
    for key, value in dict.items():
        if (type(value) == None or type(value) == bool or type(value) == int  or
                type(value) == float or type(value) == complex or list or tuple or
                type(value) == str or type(value) == bytes or type(value) == bytearray or
                type(value) == memoryview or type(value) == set or type(value) == frozenset or type(value) == dict):
            print(key, ": True")
        else:
            print(key, ": False")



