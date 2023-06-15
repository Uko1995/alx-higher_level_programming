#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary.items():
        if key is keys:
            del a_dictionary[keys]
            return a_dictionary
        else:
            return a_dictionary
