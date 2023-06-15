#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary.items():
        if key not in keys:
            return a_dictionary
        else:
            del a_dictionary[key]
            return a_dictionary
