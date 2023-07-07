#!/usr/bin/python3
'''
module that includes function for adding integers
'''


def add_integer(a, b=98):
    '''
    function returns the addition of 2 integers

    parameters:
    a: integer or float
    b: integer or float
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
