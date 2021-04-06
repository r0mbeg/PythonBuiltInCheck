def print_vars():
    varlist = [None, bool, int, float, complex, list,
               tuple, str, bytes, bytearray, memoryview,
               set, frozenset, dict]
    dictionary = sys._getframe(1).f_locals
    for key, value in dictionary.items():
        if (type(value) in varlist):
            print(key, ": True")

        else:
            print(key, ": False")


