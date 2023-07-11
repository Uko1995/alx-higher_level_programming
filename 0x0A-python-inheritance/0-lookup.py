#!/usr/bin/python3
'''
file contains lookup function
'''


def lookup(obj):
    '''
    function gets all available attributes and methods of an object

    Return: a list of all attributes and methods
    '''
    lst = []
    for item in dir(obj):
        lst.append(item)

    return lst
