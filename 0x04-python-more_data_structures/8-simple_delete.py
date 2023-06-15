#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary.items():
        if key == keys:
            del a_dictionary[key]
            return a_dictionary
        else:
            return a_dictionary
